# Brief for Helen: reducing friction for responders and handlers

**Helen,**

Responders and handlers are running into friction in the app right now. Some of it is the same problem that has four responders going quiet. We can start reducing the friction this week with app changes that don't depend on the open questions. We'll measure the rest as we go.

**The friction we're seeing**
- **Offers disappear before a responder can tap.** Responders say the phone buzzes, they reach for it, and the offer has already moved on. The shorter 60-second window made this more common.
- **Offers are hard to notice.** Small text and one shared alert sound make it hard for handlers to tell responders apart, and at night it's easy to miss a buzz.
- **Quiet responders get no explanation.** A handler can see that someone has gone quiet, but not why, and a responder who goes quiet has no way to tell whether something is wrong.

**What we don't know yet**
- Whether distance is what triggers the drop for the four responders who went quiet. We don't have location data.
- How many missed offers were timeouts versus active no's. The data can't tell them apart.

**What we're starting with**
1. **Log timeouts and no's separately.** This is the foundation. Every other decision stays a range until we have it.
2. **A grace window for near misses.** If a responder taps within a few seconds after an offer closes, it's counted as a near miss and they see a short "that one was close" message. No change to scoring, and it stops good responders from feeling punished for a late tap.
3. **A clearer offer alert.** Larger text, a high-contrast offer screen with the incident type and seconds left, and a distinct sound for each responder. This addresses the most-repeated complaints from handlers.

**Fast follows, once the logs are in**
4. **A quiet-responder alert for handlers.** It fires when a responder hasn't been offered anything for a set number of days, so a handler can act before a ticket is filed. It needs quiet hours so off-shift responders don't trigger it.
5. **A softer timeout penalty and a score bounce-back rule, tested in the simulator.** These change how scores work, so they wait for real timeout data before anything ships.

**Held for now:** a "why am I quiet?" card for responders, and an offer path to rebuild a responder's record. Until we know whether distance is the trigger, a card would be guessing at the reason, and rebuilding a record would send calls to responders who are already struggling.

**A decision for you:** whether to keep the 60-second timeout while we measure. It's a tradeoff only you can make, and it doesn't need to wait on anything else.

The prototypes are being built now, so you can see the experience before we commit to it. Each one is private until we share it.
