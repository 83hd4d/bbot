import random

adjectives = [
    "abnormal",
    "accidental",
    "acoustic",
    "acrophobic",
    "adorable",
    "adversarial",
    "affectionate",
    "aggravated",
    "aggrieved",
    "almighty",
    "anal",
    "atrocious",
    "awkward",
    "baby",
    "begrudged",
    "benevolent",
    "bewildered",
    "bighuge",
    "black",
    "blazed",
    "bloodshot",
    "brown",
    "cheeky",
    "childish",
    "chiseled",
    "cold",
    "condescending",
    "considerate",
    "constipated",
    "contentious",
    "corrupted",
    "cosmic",
    "crafty",
    "crazed",
    "creamy",
    "crispy",
    "crumbly",
    "cryptic",
    "cuddly",
    "cute",
    "dark",
    "dastardly",
    "decrypted",
    "deep",
    "delicious",
    "demented",
    "demonic",
    "depraved",
    "depressed",
    "deranged",
    "derogatory",
    "despicable",
    "devilish",
    "devious",
    "diabolic",
    "diabolical",
    "difficult",
    "dilapidated",
    "dismal",
    "distilled",
    "disturbed",
    "dramatic",
    "drunk",
    "effeminate",
    "elden",
    "eldritch",
    "embarrassed",
    "encrypted",
    "enigmatic",
    "enlightened",
    "esoteric",
    "ethereal",
    "euphoric",
    "evil",
    "exquisite",
    "extreme",
    "ferocious",
    "fiendish",
    "fierce",
    "flamboyant",
    "fleecy",
    "flirtatious",
    "flustered",
    "foreboding",
    "frenetic",
    "frolicking",
    "frothy",
    "furry",
    "fuzzy",
    "gay",
    "gentle",
    "giddy",
    "glowering",
    "glutinous",
    "golden",
    "gothic",
    "grievous",
    "gummy",
    "hallucinogenic",
    "hammered",
    "harmful",
    "heated",
    "hectic",
    "heightened",
    "heinous",
    "hellish",
    "hideous",
    "hysterical",
    "imaginary",
    "immense",
    "immoral",
    "incomprehensible",
    "inebriated",
    "inexplicable",
    "infernal",
    "ingenious",
    "inquisitive",
    "insecure",
    "insidious",
    "insightful",
    "insolent",
    "insufferable",
    "intelligent",
    "intensified",
    "intensive",
    "intoxicated",
    "inventive",
    "irritable",
    "large",
    "liquid",
    "loveable",
    "lovely",
    "lucid",
    "malevolent",
    "malfunctioning",
    "malicious",
    "manic",
    "masochistic",
    "medicated",
    "mediocre",
    "melodramatic",
    "mighty",
    "moist",
    "molten",
    "monstrous",
    "muscular",
    "mushy",
    "mysterious",
    "naughty",
    "nefarious",
    "negligent",
    "neurotic",
    "nihilistic",
    "normal",
    "overattached",
    "overcompensating",
    "overenthusiastic",
    "overmedicated",
    "overwhelming",
    "overzealous",
    "paranoid",
    "pasty",
    "pedantic",
    "pernicious",
    "perturbed",
    "perverted",
    "philosophical",
    "pillowy",
    "pink",
    "pissed",
    "pixilated",
    "plastered",
    "playful",
    "plump",
    "powerful",
    "premature",
    "profound",
    "promiscuous",
    "psychedelic",
    "psychic",
    "puffy",
    "pure",
    "queer",
    "questionable",
    "rabid",
    "raging",
    "rambunctious",
    "rapid_unscheduled",
    "raving",
    "reductive",
    "reckless",
    "ripped",
    "sadistic",
    "satanic",
    "savvy",
    "scheming",
    "schizophrenic",
    "secretive",
    "sedated",
    "senile",
    "severe",
    "shaggy",
    "sinful",
    "sinister",
    "slippery",
    "sly",
    "sneaky",
    "soft",
    "sophisticated",
    "spiteful",
    "squishy",
    "steamy",
    "sticky",
    "stoned",
    "strained",
    "strenuous",
    "stricken",
    "stubborn",
    "stuffed",
    "stumped",
    "subtle",
    "sudden",
    "suggestive",
    "sunburned",
    "surreal",
    "suspicious",
    "sweet",
    "sycophantic",
    "tense",
    "terrible",
    "terrific",
    "thick",
    "thoughtful",
    "ticklish",
    "tiny",
    "tricky",
    "twitchy",
    "ugly",
    "unabated",
    "unchained",
    "unexplained",
    "unhinged",
    "unholy",
    "unleashed",
    "unmedicated",
    "unmelted",
    "unmitigated",
    "unrelenting",
    "unrestrained",
    "unscheduled",
    "unworthy",
    "utmost",
    "vehement",
    "vicious",
    "vigorous",
    "vile",
    "violent",
    "vivid",
    "voluptuous",
    "wasted",
    "wet",
    "whimsical",
    "white",
    "wicked",
    "wild",
    "wispy",
    "witty",
    "woolly",
]

names = [
    "aaron",
    "abigail",
    "adam",
    "alan",
    "albert",
    "alex",
    "alexander",
    "alexis",
    "alice",
    "allen",
    "allison",
    "alyssa",
    "amanda",
    "amber",
    "amy",
    "andrea",
    "andrew",
    "angela",
    "ann",
    "anna",
    "anne",
    "annie",
    "anthony",
    "antonio",
    "aragorn",
    "arthur",
    "arwen",
    "ashley",
    "audrey",
    "austin",
    "azathoth",
    "baggins",
    "bailey",
    "barbara",
    "bart",
    "bellatrix",
    "benjamin",
    "betty",
    "beverly",
    "bilbo",
    "billy",
    "bobby",
    "bombadil",
    "bonnie",
    "bonson",
    "boromir",
    "bradley",
    "brandon",
    "brandybuck",
    "brenda",
    "brian",
    "brianna",
    "brittany",
    "bruce",
    "bryan",
    "caitlyn",
    "caleb",
    "cameron",
    "carl",
    "carlos",
    "carol",
    "carolyn",
    "carrie",
    "catherine",
    "charles",
    "charlotte",
    "cheryl",
    "christian",
    "christina",
    "christine",
    "christopher",
    "cindy",
    "ciri",
    "clara",
    "clarence",
    "cody",
    "connie",
    "courtney",
    "craig",
    "crystal",
    "cthulu",
    "curtis",
    "cynthia",
    "dagon",
    "dale",
    "dandelion",
    "daniel",
    "danielle",
    "danny",
    "data",
    "david",
    "dawn",
    "deborah",
    "debra",
    "deckard",
    "denethor",
    "denise",
    "dennis",
    "diana",
    "diane",
    "dobby",
    "donald",
    "donna",
    "dooku",
    "doris",
    "dorothy",
    "douglas",
    "draco",
    "dumbledore",
    "dylan",
    "earl",
    "edith",
    "edna",
    "edward",
    "elaine",
    "eleanor",
    "elendil",
    "elijah",
    "elizabeth",
    "ella",
    "ellen",
    "elrond",
    "emily",
    "emma",
    "eomer",
    "eomund",
    "eothain",
    "eowyn",
    "eric",
    "erin",
    "ernest",
    "esther",
    "ethan",
    "ethel",
    "eugene",
    "eva",
    "evan",
    "evelyn",
    "faramir",
    "florence",
    "frances",
    "francis",
    "frank",
    "fred",
    "frederick",
    "frodo",
    "gabriel",
    "galadriel",
    "gandalf",
    "gary",
    "geordi",
    "george",
    "gerald",
    "geralt",
    "gimli",
    "gladys",
    "glenn",
    "glorfindel",
    "gloria",
    "goldberry",
    "gollum",
    "grace",
    "gregory",
    "gus",
    "hagrid",
    "hannah",
    "harold",
    "harry",
    "hazel",
    "heather",
    "helen",
    "henry",
    "hermione",
    "homer",
    "howard",
    "irene",
    "isaac",
    "isabella",
    "isildur",
    "jack",
    "jacob",
    "jacqueline",
    "james",
    "jamie",
    "jane",
    "janet",
    "janice",
    "jaskier",
    "jasmine",
    "jason",
    "jayce",
    "jean",
    "jean-luc",
    "jeffrey",
    "jennifer",
    "jeremy",
    "jerry",
    "jesse",
    "jessica",
    "jimmy",
    "jinx",
    "joan",
    "joe",
    "joel",
    "john",
    "johnny",
    "jonathan",
    "jordan",
    "jose",
    "joseph",
    "josephine",
    "josh",
    "joyce",
    "juan",
    "judith",
    "judy",
    "julia",
    "julie",
    "justin",
    "karen",
    "katherine",
    "kathleen",
    "kathryn",
    "kathy",
    "kayla",
    "keith",
    "kelly",
    "kenneth",
    "kenobi",
    "kerry",
    "kevin",
    "kimberly",
    "kyle",
    "lantern",
    "larry",
    "laura",
    "lauren",
    "lawrence",
    "legolas",
    "leia",
    "leonard",
    "leslie",
    "lillian",
    "linda",
    "lisa",
    "logan",
    "lois",
    "lori",
    "louis",
    "louise",
    "lucius",
    "luis",
    "luke",
    "lupin",
    "madison",
    "magnus",
    "margaret",
    "maria",
    "marie",
    "marilyn",
    "marjorie",
    "mark",
    "martha",
    "martin",
    "marvin",
    "mary",
    "mason",
    "matthew",
    "megan",
    "melissa",
    "melvin",
    "merry",
    "michael",
    "micheal",
    "michelle",
    "mildred",
    "milhouse",
    "monica",
    "nancy",
    "natalie",
    "nathan",
    "nathaniel",
    "nazgul",
    "ned",
    "nelson",
    "nicholas",
    "nicole",
    "noah",
    "norma",
    "norman",
    "nyarlathotep",
    "obama",
    "olivia",
    "padme",
    "pamela",
    "patricia",
    "patrick",
    "paul",
    "paula",
    "peggy",
    "peter",
    "philip",
    "phillip",
    "phyllis",
    "pippin",
    "powder",
    "rachel",
    "radagast",
    "ralph",
    "rambunctious",
    "randy",
    "raymond",
    "rebecca",
    "richard",
    "rita",
    "roach",
    "robert",
    "robin",
    "rodney",
    "roger",
    "ron",
    "ronald",
    "rose",
    "ross",
    "roy",
    "ruby",
    "russell",
    "ruth",
    "ryan",
    "samantha",
    "samuel",
    "samwise",
    "sandra",
    "sara",
    "sarah",
    "saruman",
    "sauron",
    "scott",
    "sean",
    "shannon",
    "sharon",
    "shawn",
    "shelob",
    "shirley",
    "silco",
    "sirius",
    "skywalker",
    "snape",
    "sophia",
    "stanley",
    "stephanie",
    "stephen",
    "steven",
    "susan",
    "tammy",
    "taylor",
    "teresa",
    "terry",
    "theoden",
    "theresa",
    "thomas",
    "tiffany",
    "timothy",
    "tina",
    "todd",
    "tony",
    "tracy",
    "travis",
    "treebeard",
    "triss",
    "tyler",
    "tyrell",
    "vader",
    "valerie",
    "vander",
    "vanessa",
    "vi",
    "victor",
    "victoria",
    "viktor",
    "vincent",
    "virginia",
    "voldemort",
    "wallace",
    "walter",
    "wanda",
    "wayne",
    "wendy",
    "william",
    "willie",
    "worf",
    "wormtongue",
    "xavier",
    "yennefer",
    "yoda",
    "zach",
    "zachary",
]


def random_name():
    name = random.choice(names)
    adjective = random.choice(adjectives)
    if adjective == "unchained":
        scan_name = f"{name}_{adjective}"
    else:
        scan_name = f"{adjective}_{name}"
    return scan_name
