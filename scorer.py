from store import Result
import re

def normalize_text(text: str)->str:
    if not text:
        return ""
    text = re.sub(r"[^a-z0-9]+"," ", text.lower())
    text = " ".join(text.split())
    return text


def contains_phrase(haystack: str, phrase:str)->bool:
    """True when every word of `phrase` appears in `haystack`, whole-word.

    Whole words, not substrings, so the expected fact "7" doesn't match "17 30".
    """
    words = normalize_text(phrase).split()
    if not words:
        return False
    haystack_words = set(normalize_text(haystack).split())
    return all(word in haystack_words for word in words)
    


def judge(question: str, expects: str, answer: str | None, results: list[Result])->bool:
    """This function will return True when the expected fact turns up.

    The answer is checked first. If it isn't there, the retrieved chunks are
    checked too — so the verdict means "the answer said it, OR the system had
    it in hand", which is the looser of the two readings. Note that this makes
    a gate refusal score as a pass whenever the chunk contained the fact.
    """
    if question is None or expects is None:
        return False

    phrases = [part for part in re.split(r"[;|]+", expects) if part.strip()]
    if not phrases:
        return False

    if any(contains_phrase(answer or "", phrase) for phrase in phrases):
        return True

    if results:
        retrieved_text = " ".join(getattr(result, "text", "") for result in results)
        if any(contains_phrase(retrieved_text, phrase) for phrase in phrases):
            return True

    return False


def _fake_results(*texts: str)->list[Result]:
    """Stand-in chunks, so this file can be run without building the index."""
    return [
        Result(text=text, source="guide.md", label=f"guide.md#{i}",
               distance=0.4, produced_by="self-test")
        for i, text in enumerate(texts)
    ]


def main():
    """Run `python scorer.py` to watch the scorer make its calls.

    These cases cost nothing — no index, no model, no API. They are here so a
    change to the matching rules shows up immediately instead of at the end of
    the next eval run.
    """
    hospital = _fake_results("The nearest full hospital is in Brightwater, open daily.")

    # (what it is, expects, answer, chunks, what it should say)
    cases = [
        ("answer has the fact",
         "brightwater", "Head to Brightwater — it has the nearest full hospital.",
         [], True),
        ("answer misses, chunk has it",
         "brightwater", "Try the Marchwood clinic.",
         hospital, True),
        ("gate refused, chunk has it",
         "brightwater", "I don't have enough information about that.",
         hospital, True),
        ("nowhere at all",
         "trainline", "Try the Marchwood clinic.",
         hospital, False),
        ("whole words, not substrings",
         "7", "The Tuesday market starts at 17:30.",
         [], False),
        ("the same fact, written differently",
         "7", "The Tuesday market starts at 7:00 am.",
         [], True),
        ("either phrase is enough",
         "train|bus", "Take the bus from the square.",
         [], True),
    ]

    failures = 0
    for name, expects, answer, results, want in cases:
        got = judge("a question", expects, answer, results)
        ok = got == want
        failures += not ok
        print(f"  {'ok  ' if ok else 'WRONG'}  {name:32} expects={expects!r:14} -> {got}")

    print(f"\n{len(cases) - failures} of {len(cases)} cases behaved as expected.")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())



