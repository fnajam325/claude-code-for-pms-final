# 05 · Super Speed — prompts

**Context:** You joined Rook two weeks ago as PM on Dispatch.
Release 4.2 shipped on 12 August, just before you arrived, and
landed badly. You've spent three sessions finding out what went
wrong: the two piles of feedback that didn't agree, the numbers that
hid four people inside an average, and the code that settled it —
the shorter timeout is what did it.

At the end of the session, ask Claude Code to save the prompts you
wrote yourself below — not the starter prompt. The closing slide has
the exact prompt to paste. By Module 6 this file is a prompt library
built from your own questions.

---

### 1.

our director of PM pinged me asking what we're going to do? help me put together a brief.

### 2.

hmm, this feels a bit tmi for a Director. i believe there's a director-request.txt file with specific information on what the Director asked for.

### 3.

is there additional information you can gatehr from here
Rook's wiki: Rook's words, names, and the comments on the 4.2 release page.

* 00-rook/company/notes/: the note your predecessor left you.

to make for a better brief

### 4.

give me a confidence score (0-100) on how you feel about this one pager and the direction of what we need to do next? is this the right thing to prototype, or do we also need to include additional input based on the deep analysis we've been doing?

### 5.

build the simulation

### 6.

add the timeout variant and rerun it. and build the simulation as an interactive sharable artifact

### 7.

the sliders at the top are a bit of a hard grasp, rewrite at a 5th grade level

### 8.

rewrite the whole thing at a 5th grade level

### 9.

okay so looking at this simulation, now how confidence are you using the same scale?

### 10.

add the confidence score to the synthesis file

### 11.

okay we don't really have access to real data, can you develop some plausible data instead, rerun the simulation and then give me the confidence score

### 12.

got it, so what can we go back to helen with? she'll be expecting something for us to get started with?

### 13.

so what are we prototyping then?

### 14.

what other things can we prototype, and give me some judgement/impact criteron that i can weigh all options

### 15.

okay run this impact against the candidate prototypes and present them in a table so i can weigh my options. also provide me with the ones you recommend at the top

### 16.

update the helen brief to include the recommendations, and inform her that we're starting with #1, and will fast follow with #2 and #3.

### 17.

send this to slack

### 18.

commit this and push it

### 19.

save the brief

### 20.

Let's create multiple prototypes. Let's focus on the top 3 we identified. Save it under the 05-super-speed/ folder. The prototypes will need to be sharable artifacts and interactive.

Spawn multiple multiple agents so that we can build in parallel.

### 21.

what if we wanted to create some new member updates to the app to reduce friction? i was thinking the protoypes would be more along the lines of app experience

### 22.

we need to update the helen brief so that it frames this way.

### 23.

lets build interactive prototypes for candidates #1-3

### 24.

lets start with near-miss grace window. i want you play the role of these super heroes are having friction with responding to alerts. show them the prototype, ask them unbiased questions that will otherwise help us understand how effective this capability will be. once you're done, come back to me, give me their feedback, and lets determine what improvements we should make?

### 25.

Apply the four improvements to the prototype

### 26.

one thing im noticing is that the offer lacks context. i dont know how far away this incident is from me. perhaps 'phone was out of reach' isn't the right CTA, rather we need a better mechanism to flag a missed opportunity?

### 27.

yes, and then run the simulation again with 4-5 additional users, get their feedback and let me know what else we need to improve.

### 28.

apply the top three improvements to the prototype

### 29.

these are super heroes, surely they can fly or have speed right?

### 30.

why not just give the specific location and the distance from their current location

### 31.

Ask Security Policy 4.1 question

### 32.

how did we even ship 4.2 then if we cannot even flag their location or distance from such a dispatch?

### 33.

lets say security approved

### 34.

full approval

### 35.

now simulate this with users and give me feedback

### 36.

apply the first two to the prototype

### 37.

lets look at the repo, is there any design system for our app?

### 38.

i want you to be creative and rethink this ui. use bold ideas and rich super hero-like colors to design this experience.

### 39.

Read 05-super-speed/director-request.txt and explain to me what my director wants to see

What it led to: A plain explanation of Helen's ask: a fix seen from the affected person's side, not a setting, ideally clickable.

### 40.

check my brief against her ask

What it led to: The brief was compared with Helen's request, showing where it fell short.

### 41.

The note says this shouldn't just be a setting we quietly flip. Read the responder I picked from CLAUDE.md and use that name. Do not ask me which one. Walk me through what's still missing from the brief before this could actually get built.

What it led to: A list of what was missing before a build; CLAUDE.md held no recorded responder choice, which was flagged.

### 42.

lets write write the brief first before we build anything

What it led to: A first full brief for Helen, written before any prototype work.

### 43.

this brief is hard to read. let's simplify to where there's 1-2 sentences per section, we're bringing in the key data, tables are fine, and its written at the 5th grade level

What it led to: The brief was cut to short sections, tables and key data at about a 5th-grade level.

### 44.

lets organize the brief as follows: 1. executive overview 2. decisions we need from Helen 3. open item, decisions we need from other teams 4. problem we're solving for and why now 5. ideal state and plan to get there 6. supporting data 7. open questions with assigned owners

What it led to: The brief was rebuilt in the seven sections, with owners on every open question.

### 45.

pretend you are Helen, give this brief a read and provide feedback. to make sure i have a better confidence as you are playing helen i want you to do so using multiple models. don't come back to me until the different helen's are aligned and you have clear guidance on what changes we need to make to this brief.

What it led to: A multi-model Helen panel gave aligned feedback, which became brief v3.

### 46.

it feels like their analysis was using sources outside the decision brief (e.g. prototypes). assume no prototypes exist yet and have them solely judging on the brief alone

What it led to: The panel was rerun on the brief text alone, with no tools; this challenge changed the result.

### 47.

apply v3 and rerun the check

What it led to: Brief v3 was applied and the Helen panel was rerun on it.

### 48.

apply as a v4 and cut to get under one page

What it led to: Brief v4 (about one page) plus a separate reference page holding the detail.

### 49.

commit and push the v4 brief files

What it led to: The v4 brief and its reference page were saved to GitHub.

### 50.

this brief is going to serve as the input for our working prototype with the fixes. before we build anything, read the brief and ask me clarifying questions on what we to build until you are 95% confident.

What it led to: Questions answered one by one; the prototype was scoped to promises 1 and 2 as a scripted, two-device page.

### 51.

play the role of the handlers and heros and do some user testing and synthesize feedback so we can iterate on this

What it led to: Eight simulated testers (four handlers, four responders) gave feedback that merged into nine findings and a v2 change list.

### 52.

yep make them and track a change log of the changes and the reason why

What it led to: Prototype v2 was built and a change log with the reason for every change was written.

### 53.

run another round of testing with a different set of users

What it led to: Nine new testers built from real tickets found v2 had moved the blame, not removed it; that led to prototype v3.
