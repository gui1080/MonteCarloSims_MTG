import itertools, random

Muldrotha_deck = [('Land', 'Swamp'), ('Land', 'Swamp'), ('Land', 'Swamp'), ('Land', 'Swamp'), ('Land', 'Swamp'), ('Land', 'Swamp'),
        ('Land', 'Forest'), ('Land', 'Forest'), ('Land', 'Forest'), ('Land', 'Forest'), ('Land', 'Forest'),
        ('Land', 'Island'), ('Land', 'Island'), ('Land', 'Island'), ('Land', 'Island'), ('Land', 'Island'), ('Land', 'Island'), ('Land', 'Island'),
        ('Land', 'Golgari Rot Farm'), ('Land', 'Tainted Wood'), ('Land', 'Tainted Isle'), ('Land', 'Cabal Pit'), ('Land', 'Bojuka Bog'), 
        ('Land', 'Exotic Orchard'), ('Land', 'Hinterland Harbor'), ('Land', 'Ipnu Rivulet'), ('Land', 'Llanowar Wastes'),
        ('Land', 'Underground River'), ('Land', 'Evolving Wilds'), ('Land', 'Command Tower'), ('Land', 'Sunken Hollow'), ('Land', 'Terramorphic Expanse'),
        ('Artifact', 'Perpetual Timepiece'), ('Artifact', 'Nevinyrrals Disk'), ('Artifact', 'Lotus Petal'), ('Artifact', 'Sol Ring'), ('Creature', 'Birds of Paradise'), ('Artifact', 'Altar of Dementia'),
        ('Artifact', 'Possessed Portal'), ('Artifact', 'Jesters Mask'), ('Artifact', 'Chromatic Lantern'), ('Instant', 'Demonic Consultation'), ('Instant', 'Dispel'),
        ('Instant', 'Beseech the Queen'), ('Instant', 'Counterspell'), ('Instant', 'Negate'), ('Instant', 'Kodamas Reach'), ('Instant', 'Cultivate'), ('Instant', 'Buried Alive'),
        ('Instant', 'Fact or Fiction'), ('Instant', 'Diabolic Tutor'), ('Instant', 'Diabolic Revelation'), ('Siren Stormtamer', 'Creature'), 
        ('Creature', 'Satyr Wayfinder'), ('Creature', 'Priest of Titania'), ('Creature', 'Fyndhorn Elves'), ('Creature', 'Elves of Deep Shadow'), ('Creature', 'Mirror-Mad Phantasm'), ('Creature', 'Coiling Oracle'), ('Creature', 'Thassas Oracle'), ('Creature', 'Gravebreaker Lamia'),
        ('Creature', 'Stitchers Supplier'), ('Creature', 'Llanowar Elves'), ('Creature', 'Elvish Mystic'), ('Creature', 'Spore Frog'), ('Creature', 'Sakura-Tribe Elder'), ('Creature', 'Divining Witch'),
        ('Creature', 'Lord of Extinction'), ('Creature', 'Mikaeus, the Unhallowed'), ('Creature', 'Tidespout Tyrant'), ('Creature', 'Sidisi, Undead Vizier'), ('Creature', 'Doom Whisperer'), ('Creature', 'Eternal Witness'), ('Creature', 'Jarad, Golgari Lich Lord'), ('Creature', 'Tatyova, Benthic Druid'),
        ('Creature', 'Deathrite Shaman'), ('Creature', 'World Shaper'), ('Creature', 'Dreamborn Muse'), ('Creature', 'Ilysian Caryatid'), ('Planeswalker', 'Jace, Wielder of Mysteries'),
        ('Planeswalker', 'Kiora, Master of the Depths'), ('Enchantment', 'Kayas Ghostform'), ('Enchantment', 'Seal of Removal'), ('Enchantment', 'Chronic Flooding'), ('Enchantment', 'Sultai Ascendancy'), ('Enchantment', 'Khalni Heart Expedition'), 
        ('Enchantment', 'Animate Dead'), ('Enchantment', 'Pernicious Deed'), ('Enchantment', 'Rhystic Study'), ('Enchantment', 'Second Chance'), ('Enchantment', 'Defense of the Heart'),
        ('Enchantment', 'Phyrexian Scriptures'), ('Enchantment', 'Zurs Weirding')]

# random.shuffle(Muldrotha_deck)

# Opening Hand simulations!

N = 10000000

zero_land_hand = 0
one_land_hand = 0
two_land_hand = 0
three_land_hand = 0
four_land_hand = 0
five_land_hand = 0
six_land_hand = 0
seven_land_hand = 0

for hands in range(N):
    # shuffle the cards
    random.shuffle(Muldrotha_deck)
    lands = [d[0] for d in deck[0:7]].count('Land')
    if lands == 0:
        zero_land_hand+=1
    elif lands == 1:
        one_land_hand+=1
    elif lands == 2:
        two_land_hand+=1
    elif lands == 3:
        three_land_hand+=1
    elif lands == 4:
        four_land_hand+=1
    elif lands == 5:
        five_land_hand+=1      
    elif lands == 6:
        six_land_hand+=1        
    elif lands == 7:
        seven_land_hand+=1
  
        
prob0 = zero_land_hand/N
prob1 = one_land_hand/N
prob2 = two_land_hand/N
prob3 = three_land_hand/N
prob4 = four_land_hand/N
prob5 = five_land_hand/N
prob6 = six_land_hand/N   
prob7 = seven_land_hand/N


# print(Muldrotha_deck)
