"""Generates copy.json. Service copy drafted by Qwen (qwen_drafts/services_qwen_raw.json), checked and edited by Claude;
city/home/about copy written by Claude after the Qwen city draft failed the fact check (made unprovable claims).
Only fact-sheet facts or generic plumbing information. No licence/insurance/years/reviews/guarantee/pricing claims. Run: python3 copygen.py"""
import json, os
D = os.path.dirname(os.path.abspath(__file__))
sv = json.load(open(os.path.join(D, "qwen_drafts/services_qwen_raw.json")))
FIX = [("The technician", "The plumber"), ("A camera inspection is typically performed to view", "A camera inspection may be used to view"),
       ("Based on the video footage, a specific repair strategy is outlined for the homeowner.", "Once the cause is clear, the repair options are explained.")]
def fix(s):
    for a, b in FIX: s = s.replace(a, b)
    return s
PREP = "It helps to have a few details ready when you call: where in the house the problem is, when you first noticed it, and whether it is getting worse. If water is involved, say whether you have been able to shut it off. You do not need to know the cause or use plumbing terms. A plain description of what you see, hear or smell is enough to get started."
out = {}
for k, v in sv.items():
    out[k] = {"paras": [fix(v["intro"]), fix(v["visit"]), fix(v["more"]), PREP,
              "To book an appointment with {BIZ}, call. There is no online form."], "bullets": v["signs"]}
NAMES = {"johns-creek": "Johns Creek", "sandy-springs": "Sandy Springs", "alpharetta": "Alpharetta", "cumming": "Cumming", "milton": "Milton"}
SERV = "drain cleaning, water heater repair and installation, leak repair, sewer line service, toilet, faucet and fixture repair, repiping, garbage disposal repair and replacement, and emergency plumbing"
for k, n in NAMES.items():
    out[k] = {"paras": [
      f"{{BIZ}} is a plumbing company with an office in Roswell, Georgia, and {n} is one of the places it serves. If you need a plumber in {n}, call to book an appointment.",
      f"Homeowners in {n} call about the same kinds of problems that come up in any home: drains that will not clear, water heaters that stop working, leaks, running toilets and dripping faucets. Services listed on this site: {SERV}.",
      "Each service has its own page with the signs to watch for and what a visit generally involves. If you are not sure which one fits what you are seeing, describe the problem when you call and the next step can be worked out from there.",
      f"If you have a plumbing emergency in {n}, such as a burst pipe or a sewage backup, shut off the water at the main valve if you can do so safely and then call right away.",
      PREP], "bullets": []}
out["home"] = {"paras": [
 "{BIZ} is a plumbing company with an office in Roswell, Georgia. It serves homeowners in Alpharetta, Johns Creek, Sandy Springs, Cumming and Milton.",
 "Homeowners call about " + SERV + ". Each service has its own page explaining the signs to watch for and what a visit generally involves.",
 "Pick your city below to see more about plumbing service where you live. To book, call. There is no online form to fill out."], "bullets": []}
out["about"] = {"paras": [
 "{BIZ} is a plumbing company with its office at 1007 Mansell Rd #A122, Roswell, GA 30076.",
 "Plumbing is the only trade covered on this site. Services listed here are drain cleaning, water heater repair and installation, leak repair, sewer line service, toilet, faucet and fixture repair, repiping, garbage disposal repair and replacement, and emergency plumbing.",
 "The service areas are Alpharetta, Johns Creek, Sandy Springs, Cumming and Milton, Georgia. To book an appointment, call."], "bullets": []}
json.dump(out, open(os.path.join(D, "copy.json"), "w"), indent=1)
print({k: sum(len(p.split()) for p in v["paras"]) for k, v in out.items()})
