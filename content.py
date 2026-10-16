"""All words and facts for the site. Edit here, run build.py. Public repo: no private data."""
import json, os
BUSINESS_NAME = "Bluefrog Plumbing + Drain of Alpharetta"   # Brian Kingsley's own spelling (onboarding call 13 Oct 2026). Text only: no corporate logo.
PHONE = "(678) 331-5843"                   # CallScaler tracking number (bought 16 Oct 2026); forwards to the business line.
PHONE_TEL = "+16783315843"
PHONE_STATUS = "tracking number"
ADDRESS = "1007 Mansell Rd #A122, Roswell, GA 30076"
SITE_URL = "https://bluefrogplumbingofalpharetta.com"
BASE = ""
COPY = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "copy.json")))

# SERVICE LIST = PLACEHOLDER. The SEF and the onboarding call say only "plumbing". Standard residential categories used, to be confirmed with Brian.
SERVICES = [  # slug, name, short blurb
 ("drain-cleaning", "Drain Cleaning", "Clogged sinks, tubs, showers and slow drains cleared."),
 ("water-heater", "Water Heater Repair & Installation", "Repair or replace a water heater that is failing or leaking."),
 ("leak-repair", "Leak Repair", "Track down and fix dripping pipes and supply line leaks."),
 ("sewer-line", "Sewer Line Service", "Backups, slow main drains, gurgling and sewer odors."),
 ("toilet-faucet-fixtures", "Toilet, Faucet & Fixture Repair", "Running toilets, dripping faucets and worn fixtures."),
 ("repiping", "Repiping", "Replace aging supply piping in your home."),
 ("garbage-disposal", "Garbage Disposal", "Jammed, leaking or humming disposals repaired or replaced."),
 ("emergency-plumbing", "Emergency Plumbing", "Burst pipes, major leaks, overflowing toilets and backups."),
]
AREAS = [  # slug, city  (Johns Creek and Sandy Springs first: most open per market research)
 ("johns-creek", "Johns Creek"), ("sandy-springs", "Sandy Springs"), ("alpharetta", "Alpharetta"), ("cumming", "Cumming"), ("milton", "Milton"),
]
WHY = [
 ("Plumbing only", "Plumbing is the only trade on this site. Every call is a plumbing call."),
 ("Call to book", "Reach us by phone and book an appointment."),
 ("Clear service pages", "Each service page explains the signs to watch for and what a visit generally involves."),
 ("North Fulton and Forsyth", "Serving Alpharetta, Johns Creek, Sandy Springs, Cumming and Milton."),
]
