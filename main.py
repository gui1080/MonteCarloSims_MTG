
import itertools, random

Muldrotha_deck = [('Swamp', 'Land'), ('Swamp', 'Land'), ('Swamp', 'Land'), ('Swamp', 'Land'), ('Swamp', 'Land'), ('Swamp', 'Land'),
        ('Forest', 'Land'), ('Forest', 'Land'), ('Forest', 'Land'), ('Forest', 'Land'), ('Forest', 'Land'),
        ('Island', 'Land'), ('Island', 'Land'), ('Island', 'Land'), ('Island', 'Land'), ('Island', 'Land'), ('Island', 'Land'), ('Island', 'Land'),
        ('Golgari Rot Farm', 'Land'), ('Tainted Wood', 'Land'), ('Tainted Isle', 'Land'), ('Cabal Pit', 'Land'), ('Bojuka Bog', 'Land'), 
        ('Exotic Orchard', 'Land'), ('Hinterland Harbor', 'Land'), ('Ipnu Rivulet', 'Land'), ('Llanowar Wastes', 'Land'),
        ('Underground River', 'Land'), ('Evolving Wilds', 'Land'), ('Command Tower', 'Land'), ('Sunken Hollow', 'Land'), ('Terramorphic Expanse', 'Land'),
        ('Perpetual Timepiece', 'Artifact'), ('Nevinyrrals Disk', 'Artifact'), ('Lotus Petal', 'Artifact'), ('Sol Ring', 'Artifact'), ('AEther Spellbomb', 'Artifact'), ('Altar of Dementia', 'Artifact'),
        ('Possessed Portal', 'Artifact'), ('Jesters Mask', 'Artifact'), ('Chromatic Lantern', 'Artifact'), ('Demonic Consultation', 'Instant'), ('Dispel', 'Instant'),
        ('Beseech the Queen', 'Instant'), ('Counterspell', 'Instant'), ('Negate', 'Instant'), ('Kodamas Reach', 'Instant'), ('Cultivate', 'Instant'), ('Buried Alive', 'Instant'),
        ('Fact or Fiction', 'Instant'), ('Diabolic Tutor', 'Instant'), ('Diabolic Revelation', 'Instant'), ('Siren Stormtamer', 'Creature'), 
        ('Satyr Wayfinder', 'Creature'), ('Priest of Titania', 'Creature'), ('Fyndhorn Elves', 'Creature'), ('Consuming Aberration', 'Creature'), ('Mirror-Mad Phantasm', 'Creature'), ('Coiling Oracle', 'Creature'), ('Thassas Oracle', 'Creature'), ('Gravebreaker Lamia', 'Creature'),
        ('Stitchers Supplier', 'Creature'), ('Llanowar Elves', 'Creature'), ('Elvish Mystic', 'Creature'), ('Spore Frog', 'Creature'), ('Sakura-Tribe Elder', 'Creature'), ('Divining Witch', 'Creature'),
        ('Lord of Extinction', 'Creature'), ('Mikaeus, the Unhallowed', 'Creature'), ('Tidespout Tyrant', 'Creature'), ('Sidisi, Undead Vizier', 'Creature'), ('Doom Whisperer', 'Creature'), ('Eternal Witness', 'Creature'), ('Jarad, Golgari Lich Lord', 'Creature'), ('Tatyova, Benthic Druid', 'Creature'),
        ('Deathrite Shaman', 'Creature'), ('World Shaper', 'Creature'), ('Dreamborn Muse', 'Creature'), ('Ilysian Caryatid', 'Creature'), ('Jace, Wielder of Mysteries', 'Planeswalker'),
        ('Kiora, Master of the Depths', 'Planeswalker'), ('Kayas Ghostform', 'Enchantment'), ('Seal of Removal', 'Enchantment'), ('Chronic Flooding', 'Enchantment'), ('Sultai Ascendancy', 'Enchantment'), ('Khalni Heart Expedition', 'Enchantment'), 
        ('Animate Dead', 'Enchantment'), ('Pernicious Deed', 'Enchantment'), ('Rhystic Study', 'Enchantment'), ('Second Chance', 'Enchantment'), ('Defense of the Heart', 'Enchantment'),
        ('Phyrexian Scriptures', 'Enchantment'), ('Zurs Weirding', 'Enchantment')]

random.shuffle(Muldrotha_deck)

print(Muldrotha_deck)
