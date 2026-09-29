# The Unofficial Guide



> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

Suman Karki city_guides

# Unit 1

## What This Does
<!-- Three or four sentences. Which corpus you picked, and the kinds of
     questions your system answers. Write it for someone who has never seen
     this repo.

     Milestone 5. -->
I selected city_guide, my system can answer questions about travel, local logistics, food, walking routes, and practical visitor advice for the fictional region about those nine towns. They can answer like What are the transportation options,  parking available or not, travel times etc. It can also answer food/dining and can answer cheaper/better value food options. 


## Chunking Strategy

**Chunk size:**
**Overlap:**

Chunk size 700
Overlap: 0

<!-- What about YOUR documents made you pick these numbers? Short posts and
     long sectioned guides don't want the same chunking, and "800 seemed
     reasonable" earns nothing. Point at something you noticed when you read
     the documents in Milestone 1.
**Chunk size:** Up to three complete body sentences, with the document title repeated for context.

     If you changed your mind partway through, say so and say why. That's worth
     more than pretending you got it right first time.
**Overlap:** Zero repeated body sentences; the title is retained in each chunk.

     Milestone 3. -->
My documents are organized well with topics and paragraphs.Essentially, answers can be found with in the paragraph so I decided to chunk using paragraph and upper limit of the chunks size about 700. Overlap I keept 0, I decided not to reuse text from the previous chunk. 


## Sample Chunks

<!-- Five chunks, pasted as text. Label each one and name the file it came from
     AND the function that produced it — the grader checks your code against
     what you claim here.

     `python app.py chunks -n 5` prints all three for you. Copy them straight
     across.

     Milestone 3. -->

**Chunk 1** — source: `guide_accessibility.md#0` — produced by: `chunker.py::split_documents`

```
# Getting around the region with limited mobility

An honest assessment rather than a promotional one. Some of these places are
difficult and it is better to know in advance.

## Straightforward

**Thornby Wells** is the easiest town in the region. It is flat, compact, and
everything is within three minutes of everything else. Parking is free for two
hours anywhere in town and the station is central. The pump room and gardens
are level throughout.

**Marchwood** has a modern tram network with level boarding on all four lines,
running every 8 minutes on weekdays. The city museum and covered market are both
step-free. The distances between districts are the main consideration.
```

**Chunk 2** — source: `guide_corry_vale.md#2` — produced by: `chunker.py::split_documents`

```
The valley itself is the attraction. The footpath network is dense and well marked, and a circuit taking in three of the four villages is about nine miles with 500 metres of ascent. The chapel in the second village is 12th century and always unlocked.

## Where to stay

Perhaps thirty beds in the entire valley, spread across two pubs and a handful of farmhouse rooms. In summer these are booked months ahead. Camping is permitted on two marked fields and nowhere else.

## When to go
```

**Chunk 3** — source: `guide_givens_mill.md#0` — produced by: `chunker.py::split_documents`

```
# Givens Mill

Givens Mill is a village of 700 built around a working watermill that still grinds flour commercially. It is the sort of place people visit for an afternoon and then talk about for longer than the visit lasted.

## Getting there

No station and no bus on Sundays; four buses a day from Brightwater on weekdays, taking 30 minutes. Driving is 20 minutes. The village car park holds about forty cars and is full by 11am on summer Saturdays.

## Getting around

Everything is on one street along the river. The mill is at one end and the church at the other, eight minutes apart. The riverside path continues in both directions for as far as you want to walk.

## Eat and drink
```

**Chunk 4** — source: `guide_kestrelford.md#3` — produced by: `chunker.py::split_documents`

```
Late spring and early autumn. The Saturday market runs year-round but is much reduced from November to February. August is busy with walkers. The single-track approach road is genuinely difficult in snow and the town can be cut off for a day or two most winters.

## Practical notes

Cash is still useful at the market and in smaller places, though cards are
accepted almost everywhere now. Mobile coverage is good in the centre and
patchy on the outskirts. The nearest full hospital is in Brightwater; there is
a minor injuries unit locally with limited hours.

```

**Chunk 5** — source: `guide_regional_transport.md#1` — produced by: `chunker.py::split_documents`

```
Three operators run in the region and they do not accept each other's tickets,
which is the single most common source of confusion for visitors. Services
concentrate on weekday daytimes. Sunday service is minimal to non-existent
outside the Brightwater town routes.

The Kestrelford service is hourly on weekdays, two-hourly on Saturdays, and
does not run on Sundays. The Halden Bay coast service runs four times daily
year-round.

## Driving

For each one, ask: could someone answer a question using only this,
without reading what came before or after?
```

## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

**Question:**
If I want to suggest the easy town for my grandmother what is the best town I am looking for flat easy to walk?
**Answer:**

```
The easiest town in the region is Thornby Wells because it is flat, compact, and everything is within three minutes of everything else, with level pump rooms and gardens (guide_accessibility.md).
```

**My relevance cutoff:**

<!-- The number you set in config.py, and how you got there.

     You ran five questions your corpus covers and the five in OUT_OF_SCOPE
     that it clearly doesn't, and wrote down the best distance for each. What
     did those two groups look like? Where was the gap? Put the actual numbers
     here — the table below wants all ten rows.

     Milestone 4. -->

| Question | In corpus? | Best distance |
|---|---|---|
|What is the best way to get from Brightwater to the regional hub?|Yes| 0.372|
|If I wanted to have a meal on Sunday evening what is the place you suggest|Yes|0.487|
|If I am going to Marchwood and do some shoping what is the best payment options|Yes|0.531|
|I would like to go to Brightwater for Tuesday market what time the Tuesday market starts?|Yes|0.257|
|Where does one has to go to find nearest full hospital if you are in Givens Mill?|Yes|0.389|
|What is the capital of Mongolia?|No|0.845|
|How do I change the oil in a diesel engine?|No|0.911|
|Who won the 1994 World Cup?|No|1.008|
|What is the recommended dosage of ibuprofen for a headache?|No|0.85|
|How do I write a for loop in Rust?|No|0.819|

## How I Used AI

<!-- Two specific moments. For each: what you asked for, what came back, and
     what you changed about it.

     "I asked Claude to write the chunking function from my notes. It ignored
     the overlap, so I added that myself" is the level of detail we're after.
     "I used AI to help me code" is not.

     Milestone 5. -->

**1.**
I ask Claude to give me the summary of what each program does in this repo to understand.

**2.**

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 4/5 | 4/5 | 4/5  | MET |
| 2. Every answer names a source | 5 of 5 | 4/5  | 4/5 | 4/5 | MISSED |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4.No chunk under 40 or over 700 characters| 53 of 53| 53/53 | 53/53 | 53/53 | MET |
| 5. the answer includes the correct town or route name| 4 of 5 | 3/5| 3/5 | 3/5 | MISSED |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

### Criterion 1 — Retrieved chunk contains the answer (4/5)

- Produced by: `run_eval.py::main`
- Retrieval: `store.py::search`, chunks from `chunker.py::split_documents`

### Where does one has to go to find nearest full hospital if you are in Givens Mill? — run 1

- Best distance: 0.3891 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_corry_vale.md, guide_givens_mill.md, guide_marchwood.md

```
According to the documents, the nearest full hospital is in Brightwater (guide_givens_mill.md).
```

### I would like to go to Brightwater for Tuesday market what time the Tuesday market starts? — run 1

- Best distance: 0.2574 (passed the gate)
- Sources retrieved: guide_brightwater.md, guide_eating.md, guide_kestrelford.md, guide_regional_transport.md, guide_seasons.md

```
The Brightwater Tuesday market sets up at 7am. 

Sources: `guide_eating.md` and `guide_brightwater.md`
```

### Criterion 2 — Every answer names a source (4/5, MISSED)

Produced by: `generate.py::answer_from_chunks`

### What is the best way to get from Brightwater to the regional hub? — run 2

- Best distance: 0.3716 (passed the gate)
- Sources retrieved: guide_brightwater.md, guide_kestrelford.md, guide_regional_transport.md, guide_walking.md

```
Based on the provided documents, the train is the best way to get from Brightwater to the regional hub, taking 50 minutes with eleven services a day on weekdays and six on Sundays (*guide_regional_transport.md* and *guide_brightwater.md*).
```
### If I am going to Marchwood and do some shoping what is the best payment options — run 1

- Best distance: 0.5306 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_eating.md, guide_kestrelford.md, guide_marchwood.md, guide_thornby_wells.md

```
I do not have enough information to answer this question about shopping payment options in Marchwood, as the provided documents do not mention payment methods for Marchwood.
```

## The relevance gate on out-of-corpus questions

Produced by `run_eval.py::check_out_of_scope`, cutoff 0.65. Refused 5 of 5.

Retrieval is deterministic and the gate is a comparison against a
fixed number, so these do not vary between runs — one pass over the
list is the whole measurement.

| Out-of-scope question | Best distance | Gate |
|---|---|---|
| What is the capital of Mongolia? | 0.845 | refused |
| How do I change the oil in a diesel engine? | 0.911 | refused |
| Who won the 1994 World Cup? | 1.008 | refused |
| What is the recommended dosage of ibuprofen for a headache? | 0.858 | refused |
| How do I write a for loop in Rust? | 0.819 | refused |


### Criterion 4 — No chunk under 40 or over 700 characters (5/5, MET)

Produced by: `chunker.py::describe`, over the chunks from `chunker.py::split_documents`
(run with `python chunker.py`)

```
53 chunks, 544 characters on average (shortest 131, longest 696), produced by chunker.py::split_documents
```

### Criterion 5 — The answer includes the correct town or route name (3/5, MISSED)

Produced by: `generate.py::answer_from_chunks`

### If I wanted to have a meal on Sunday evening what is the place you suggest — run 1

- Best distance: 0.4874 (passed the gate)
- Sources retrieved: guide_brightwater.md, guide_eating.md, guide_elder_ness.md, guide_pellew_sands.md

```
Based on the documents, Sunday evening is hardest to find anywhere except in Marchwood and Thornby Wells (`guide_eating.md`).
```

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunk contains the answer | MET | Target 4 of 5. All three runs came out 4/5, so the target held every time rather than once. The same question missed in all three runs (Tuesday market time), so the 4 is stable. |
| 2 | Every answer names a source | MISSED | Target was 5 of 5. Four named a document; the Marchwood payment question returned "I do not have enough information" and cited nothing. So 4/5 is a miss by definition, not a near-miss. I counted it as a miss even though refusing was the right behaviour, because this criterion is about naming a source, not about being right. |
| 3 | Gate stops out-of-corpus questions | MET | Target 4 of 5; the gate refused 5 of 5. Measured in one pass rather than three because retrieval is deterministic and the gate is a comparison against a fixed number (0.65), so there is nothing that could vary between runs. The closest out-of-scope distance was 0.819, well clear of the cutoff. |
| 4 | No chunk under 40 or over 700 characters | MET | Shortest chunk 131 characters, longest 696, measured across all 53 chunks, all where between lower and upper chunk limit |
| 5 | Answer includes the correct town or route name | MISSED | arget 4 of 5; got 3/5 in all three runs. My scoring rule: a town name only counts if the answer drew it from the guides, not if it echoed a place I named in my own question. That is what failed the Marchwood payment answer — "Marchwood" appears in it, but only because I put it there. |


## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

Both misses are the same problem at the same stage: chunking. My chunker
drops the document title, so the town a chunk belongs to is usually not inside
the chunk. Every fact in my corpus is town-scoped, and my chunks are not.

Two of my five questions need a fact that only makes sense when paired with a
town name, and in both cases the pairing was destroyed at chunking time. They
are one problem, not two.

One other problem I notice is for the crietrion 1 it missed  
My question about the Tuesday market has expects: "7" in questions.py. But every run answer said "7am".

### A measurement problem I found while diagnosing this

Criterion 1's one miss is not a pipeline failure. My question about the Tuesday
market has `expects: "7"` in `questions.py`. The corpus says "sets up in the
square from 7am" and all three of my answers said "7am". My scorer.py::contains_phrase matches whole words rather than substrings so "7" never matches "7am" and the question scored fail in all three runs despite being
answered correctly every time.


## The Improvement

**What I changed:**

I changed chunker.py::split_documents to prepend the document's title line to
every chunk it produces, instead of only to the first one. 

I also had to reduce the accumulation budget from 700 characters to
700 - len(title prefix), because my longest chunk was already 696 characters
and adding a title would have pushed it past the upper bound I set in criterion 4. 

**Why I picked it:**

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->
Both of my misses trace to the same mechanism; a town scoped fact sitting in a
chunk that does not name its town and putting the title in every chunk is the
smallest change that puts the missing half back where the embedding can see it.

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 4/5 | 4/5 | 4/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5  | 5/5  | MET  |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5  | MET |
| 4. | No chunk under 40 or over 700 characters | all chuncks| 55/55 | 55/55 | 55/55 | MET | 
| 5. The answer includes the correct town or route name | 4 of 5 | 4/5 | 4/5  | MET |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

For criterion 2 the question that was failing now answers correctly. Before, this question refused and cited nothing. After, all three runs answer
from the right document. 
Before the changes there were 53 chunks but not there has been 55 chunks (details: 55 chunks, 541 characters on average (shortest 159, longest 695), produced by chunker.py::split_documents). Approparetly added the title from the document if presented otherwise the document source. 

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->
