# Brief for Helen: quiet-responder problem

**Helen,**

Here's where we are on the quiet-responder problem, and what we're starting with.

**What we're confident about**
- Four responders (Farlight, Meteor Mite, The Undertow, Vesper) dropped from about 12 offers a week to 0–1 after 4.2 and haven't recovered. Two more (Ashgrove, Halfmoon) are slipping in a different way.
- Once someone misses offers, their score can't recover on its own. Nothing in the code raises it except saying yes.

**What we don't know yet**
- Whether distance is what triggers the drop. We don't have location data.
- How many missed offers were timeouts versus active no's. The weekly data can't tell them apart, and that changes how much a softer timeout would help.

**What we're starting with, and why**
1. **Log timeouts and no's separately.** This is the cheapest step and fills the biggest gap. Every other answer stays a range until we have it.
2. **Fast follow: a softer timeout penalty, tested in the simulator.** It's the strongest lever we've found, and it can be tested without changing the live system. Once the logs exist, we swap in the real split.
3. **Fast follow: a score bounce-back rule, tested in the simulator.** A bounce back alone isn't enough, but it may be part of the answer, and testing it is cheap.

**Later:** a delivery check for the nine "quiet" responders, which needs telemetry access, and the handler-side explanation and responder re-entry path, once we know whether distance is the trigger. We're holding off on those because the re-entry path would push calls onto responders who are already struggling.

**A decision for you:** whether to keep the 60-second timeout while we measure. It's a tradeoff only you can make, and it doesn't need to wait on anything else.

The simulator is here if you want to see the options: https://claude.ai/artifact/1ZbzXkgzC87vt7DP3PD9Ya. It's a sandbox for testing rules, not a forecast. Its results depend on the missing timeout split, so treat them as a range.
