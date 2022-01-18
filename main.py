import itertools, random

#-------------------------------- 1 --------------------------------

Muldrotha_deck = [('Creature', 'Llanowar Elves'), ('Creature', 'Walking Ballista'), ('Creature', 'Birds of Paradise'), ('Creature', 'Siren Stormtamer'), ('Creature', 'Elves of Deep Shadow'),
('Creature', 'Fyndhorn Elves'), ('Creature', 'Stitchers Supplier'), ('Creature', 'Elvish Mystic'), ('Creature', 'Spore Frog'), ('Creature', 'Deathrite Shaman'), 
('Creature', 'Sakura-Tribe Elder'), ('Creature', 'Divining Witch'), ('Creature', 'Ilysian Caryatid'), ('Creature', 'Coiling Oracle'), ('Creature', 'Thassas Oracle'),
('Creature', 'Satyr Wayfinder'), ('Creature', 'Priest of Titania'), ('Creature', 'Eternal Witness'), ('Creature', 'Llanowar Visionary'),  ('Creature', 'Jarad, Golgari Lich Lord'),
('Creature', 'World Shaper'), ('Creature', 'Dreamborn Muse'), ('Creature', 'Mirror-Mad Phantasm'), ('Creature', 'Gravebreaker Lamia'), ('Creature', 'Lord of Extinction'),
('Creature', 'Sidisi, Undead Vizier'), ('Creature', 'Doom Whisperer'), ('Creature', 'Tatyova, Benthic Druid'), ('Creature', 'Mikaeus, the Unhallowed'), ('Creature', 'Tidespout Tyrant'),
('Planeswalker', 'Jace, Wielder of Mysteries'), ('Instant', 'Demonic Consultation'), ('Instant', 'Dispel'), ('Instant', 'Counterspell'), ('Instant', 'Negate'), ('Instant', 'Kodamas Reach'), 
('Instant', 'Cultivate'), ('Instant', 'Buried Alive'), ('Instant', 'Diabolic Tutor'), ('Instant', 'Diabolic Revelation'), ('Instant', 'Fact or Fiction'), ('Instant', 'Beseech the Queen'), 
('Artifact', 'Lotus Petal'), ('Artifact', 'Sol Ring'), ('Artifact', 'Altar of Dementia'), ('Artifact', 'Perpetual Timepiece'), ('Artifact', 'Chromatic Lantern'), ('Artifact', 'Nevinyrrals Disk'), 
('Artifact', 'Jesters Mask'), ('Artifact', 'Possessed Portal'), ('Enchantment', 'Kayas Ghostform'), ('Enchantment', 'Seal of Removal'), ('Enchantment', 'Chronic Flooding'), ('Enchantment', 'Khalni Heart Expedition'),
('Enchantment', 'Animate Dead'), ('Enchantment', 'Sultai Ascendancy'), ('Enchantment', 'Pernicious Deed'), ('Enchantment', 'Rhystic Study'), ('Enchantment', 'Second Chance'), ('Enchantment', 'Defense of the Heart'),
('Enchantment', 'Phyrexian Scriptures'), ('Enchantment', 'Zurs Weirding'), ('Land_no_Mana', 'Glacial Chasm'), ('Land', 'Dimir Aqueduct'), ('Land', 'Yavimaya Coast'), ('Land', 'Choked Estuary'), 
('Land', 'Forest'), ('Land', 'Forest'), ('Land', 'Forest'), ('Land', 'Forest'), ('Land', 'Forest'), ('Land', 'Forest'), ('Land', 'Tainted Wood'), ('Land', 'Island'), ('Land', 'Island'), ('Land', 'Island'),
('Land', 'Island'), ('Land', 'Island'), ('Land', 'Island'), ('Land', 'Island'), ('Land', 'Tainted Isle'), ('Land', 'Cabal Pit'), ('Land', 'Swamp'), ('Land', 'Swamp'), ('Land', 'Swamp'), ('Land', 'Swamp'), ('Land', 'Swamp'), ('Land', 'Swamp'),
('Land', 'Swamp'), ('Land', 'Bojuka Bog'), ('Land', 'Exotic Orchad'), ('Land', 'Hinterland Harbor'), ('Land', 'Ipnu Rivulet'), ('Land', 'Llanowar Wastes'), ('Land', 'Underground River'), ('Land', 'Evolving Wilds'),
('Land', 'Command Tower'), ('Land', 'Sunken Hollow'), ('Land', 'Terramorphic Expanse')]   

# print(len(Muldrotha_deck))

# random.shuffle(Muldrotha_deck)

# Opening Hand simulations!

N = 1000000

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
    # print("Simulation 1 -> Hand ", hands, "!")
    random.shuffle(Muldrotha_deck)
    lands = [d[0] for d in Muldrotha_deck[0:7]].count('Land')
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


print("----------------Simulation 1----------------")
print("Zero land hand probability: ", prob0)
print("One land hand probability: ", prob1)
print("Two land hand probability: ", prob2)
print("Three land hand probability: ", prob3)
print("Four land hand probability: ", prob4)
print("Five land hand probability: ", prob5)
print("Six land hand probability: ", prob6)
print("Seven land hand probability: ", prob7)



#-------------------------------- 2 --------------------------------


# Opening Hand simulations + 3 turns
# "Should I Mulligan?" analysis 

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
    # print("Simulation 1 -> Hand ", hands, "!")
    random.shuffle(Muldrotha_deck)
    lands = [d[0] for d in Muldrotha_deck[0:10]].count('Land')
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


print("----------------Simulation 2----------------")
print("Zero land hand probability: ", prob0)
print("One land hand probability: ", prob1)
print("Two land hand probability: ", prob2)
print("Three land hand probability: ", prob3)
print("Four land hand probability: ", prob4)
print("Five land hand probability: ", prob5)
print("Six land hand probability: ", prob6)
print("Seven land hand probability: ", prob7)

#-------------------------------- 2 , but considering other mana producing cards --------------------------------

# PM -> Produces Mana
# LPM -> Land that Produces Mana
# CM -> Costs Mana
# P -> Protection (Glacial Chasm is a land that does not produce mana)

Muldrotha_deck = [('PM', 'Llanowar Elves'), ('CM', 'Walking Ballista'), ('PM', 'Birds of Paradise'), ('CM', 'Siren Stormtamer'), ('PM', 'Elves of Deep Shadow'),
('PM', 'Fyndhorn Elves'), ('CM', 'Stitchers Supplier'), ('PM', 'Elvish Mystic'), ('CM', 'Spore Frog'), ('PM', 'Deathrite Shaman'), 
('PM', 'Sakura-Tribe Elder'), ('CM', 'Divining Witch'), ('PM', 'Ilysian Caryatid'), ('CM', 'Coiling Oracle'), ('CM', 'Thassas Oracle'),
('CM', 'Satyr Wayfinder'), ('PM', 'Priest of Titania'), ('CM', 'Eternal Witness'), ('PM', 'Llanowar Visionary'),  ('CM', 'Jarad, Golgari Lich Lord'),
('CM', 'World Shaper'), ('CM', 'Dreamborn Muse'), ('CM', 'Mirror-Mad Phantasm'), ('CM', 'Gravebreaker Lamia'), ('CM', 'Lord of Extinction'),
('CM', 'Sidisi, Undead Vizier'), ('CM', 'Doom Whisperer'), ('CM', 'Tatyova, Benthic Druid'), ('CM', 'Mikaeus, the Unhallowed'), ('CM', 'Tidespout Tyrant'),
('CM', 'Jace, Wielder of Mysteries'), ('CM', 'Demonic Consultation'), ('CM', 'Dispel'), ('CM', 'Counterspell'), ('CM', 'Negate'), ('PM', 'Kodamas Reach'), 
('PM', 'Cultivate'), ('CM', 'Buried Alive'), ('CM', 'Diabolic Tutor'), ('CM', 'Diabolic Revelation'), ('CM', 'Fact or Fiction'), ('CM', 'Beseech the Queen'), 
('PM', 'Lotus Petal'), ('PM', 'Sol Ring'), ('CM', 'Altar of Dementia'), ('CM', 'Perpetual Timepiece'), ('PM', 'Chromatic Lantern'), ('CM', 'Nevinyrrals Disk'), 
('CM', 'Jesters Mask'), ('CM', 'Possessed Portal'), ('CM', 'Kayas Ghostform'), ('CM', 'Seal of Removal'), ('CM', 'Chronic Flooding'), ('PM', 'Khalni Heart Expedition'),
('CM', 'Animate Dead'), ('CM', 'Sultai Ascendancy'), ('CM', 'Pernicious Deed'), ('CM', 'Rhystic Study'), ('CM', 'Second Chance'), ('CM', 'Defense of the Heart'),
('CM', 'Phyrexian Scriptures'), ('CM', 'Zurs Weirding'), ('P', 'Glacial Chasm'), ('LPM', 'Dimir Aqueduct'), ('LPM', 'Yavimaya Coast'), ('LPM', 'Choked Estuary'), 
('LPM', 'Forest'), ('LPM', 'Forest'), ('LPM', 'Forest'), ('LPM', 'Forest'), ('LPM', 'Forest'), ('LPM', 'Forest'), ('LPM', 'Tainted Wood'), ('LPM', 'Island'), ('LPM', 'Island'), ('LPM', 'Island'),
('LPM', 'Island'), ('LPM', 'Island'), ('LPM', 'Island'), ('LPM', 'Island'), ('LPM', 'Tainted Isle'), ('LPM', 'Cabal Pit'), ('LPM', 'Swamp'), ('LPM', 'Swamp'), ('LPM', 'Swamp'), ('LPM', 'Swamp'), ('LPM', 'Swamp'), ('LPM', 'Swamp'),
('LPM', 'Swamp'), ('LPM', 'Bojuka Bog'), ('LPM', 'Exotic Orchad'), ('LPM', 'Hinterland Harbor'), ('LPM', 'Ipnu Rivulet'), ('LPM', 'Llanowar Wastes'), ('LPM', 'Underground River'), ('LPM', 'Evolving Wilds'),
('LPM', 'Command Tower'), ('LPM', 'Sunken Hollow'), ('LPM', 'Terramorphic Expanse')] 

# Opening Hand simulations + 3 turns
# "Should I Mulligan?" analysis 

zero_mana_hand = 0
one_mana_hand = 0
two_mana_hand = 0
three_mana_hand = 0
four_mana_hand = 0
five_mana_hand = 0
six_mana_hand = 0
seven_mana_hand = 0


for hands in range(N):
    # shuffle the cards
    # print("Simulation 1 -> Hand ", hands, "!")
    random.shuffle(Muldrotha_deck)
    initial_LPM = [d[0] for d in Muldrotha_deck[0:10]].count('LPM')
    initial_PM = [d[0] for d in Muldrotha_deck[0:10]].count('PM')

    mana = initial_LPM + initial_PM

    if mana == 0:
        zero_mana_hand+=1
    elif mana == 1:
        one_mana_hand+=1
    elif mana == 2:
        two_mana_hand+=1
    elif mana == 3:
        three_mana_hand+=1
    elif mana == 4:
        four_mana_hand+=1
    elif mana == 5:
        five_mana_hand+=1      
    elif mana == 6:
        six_mana_hand+=1        
    elif mana == 7:
        seven_mana_hand+=1
  
        
prob0 = zero_mana_hand/N
prob1 = one_mana_hand/N
prob2 = two_mana_hand/N
prob3 = three_mana_hand/N
prob4 = four_mana_hand/N
prob5 = five_mana_hand/N
prob6 = six_mana_hand/N   
prob7 = seven_mana_hand/N


print("----------------Simulation 2----------------")
print("Zero mana hand probability: ", prob0)
print("One mana hand probability: ", prob1)
print("Two mana hand probability: ", prob2)
print("Three mana hand probability: ", prob3)
print("Four mana hand probability: ", prob4)
print("Five mana hand probability: ", prob5)
print("Six mana hand probability: ", prob6)
print("Seven mana hand probability: ", prob7)


#-------------------------------- 3 --------------------------------

no_muldrotha_zero_land_hand = 0
no_muldrotha_one_land_hand = 0
no_muldrotha_two_land_hand = 0
no_muldrotha_three_land_hand = 0
no_muldrotha_four_land_hand = 0
no_muldrotha_five_land_hand = 0
no_muldrotha_six_land_hand = 0
no_muldrotha_seven_land_hand = 0

muldrotha_zero_land_hand = 0
muldrotha_one_land_hand = 0
muldrotha_two_land_hand = 0
muldrotha_three_land_hand = 0
muldrotha_four_land_hand = 0
muldrotha_five_land_hand = 0
muldrotha_six_land_hand = 0
muldrotha_seven_land_hand = 0

muldrotha_in_play = 0
no_muldrotha = 0

mana_more_than_6 = 0
mana_less_than_6 = 0

for hands in range(N):
    # shuffle the cards
    random.shuffle(Muldrotha_deck)
    LPM = [d[0] for d in Muldrotha_deck[0:10]].count('LPM')
    PM = [d[0] for d in Muldrotha_deck[0:10]].count('LPM')
    initial_hand_LPM = [d[0] for d in Muldrotha_deck[0:10]].count('LPM')
    initial_hand_PM = [d[0] for d in Muldrotha_deck[0:10]].count('PM')
        
    mana = LPM + PM
    initial_mana = initial_hand_PM + initial_hand_LPM

    if mana >= 6 :
        
        muldrotha_in_play += 1

        mana_more_than_6 += 1
        
        if initial_mana == 0:
                muldrotha_zero_land_hand+=1
        elif initial_mana == 1:
                muldrotha_one_land_hand+=1
        elif initial_mana == 2:
                muldrotha_two_land_hand+=1
        elif initial_mana == 3:
                muldrotha_three_land_hand+=1
        elif initial_mana == 4:
                muldrotha_four_land_hand+=1
        elif initial_mana == 5:
                muldrotha_five_land_hand+=1      
        elif initial_mana == 6:
                muldrotha_six_land_hand+=1        
        elif initial_mana == 7:
                muldrotha_seven_land_hand+=1
                
    else:
        
        no_muldrotha += 1

        mana_less_than_6 += 1
        
        if initial_mana == 0:
                no_muldrotha_zero_land_hand+=1
        elif initial_mana == 1:
                no_muldrotha_one_land_hand+=1
        elif initial_mana == 2:
                no_muldrotha_two_land_hand+=1
        elif initial_mana == 3:
                no_muldrotha_three_land_hand+=1
        elif initial_mana == 4:
                no_muldrotha_four_land_hand+=1
        elif initial_mana == 5:
                no_muldrotha_five_land_hand+=1      
        elif initial_mana == 6:
                no_muldrotha_six_land_hand+=1        
        elif initial_mana == 7:
                no_muldrotha_seven_land_hand+=1
        
# Muldrotha playable, turn 3
prob_muldrotha_in_play = muldrotha_in_play/N
prob_no_muldrotha = no_muldrotha/N

# Since Muldrotha was Playable, initial hand was

prob_muldrotha_zero_land_hand = muldrotha_zero_land_hand/mana_more_than_6
prob_muldrotha_one_land_hand = muldrotha_one_land_hand/mana_more_than_6
prob_muldrotha_two_land_hand = muldrotha_two_land_hand/mana_more_than_6
prob_muldrotha_three_land_hand = muldrotha_three_land_hand/mana_more_than_6
prob_muldrotha_four_land_hand = muldrotha_four_land_hand/mana_more_than_6
prob_muldrotha_five_land_hand = muldrotha_five_land_hand/mana_more_than_6
prob_muldrotha_six_land_hand = muldrotha_six_land_hand/mana_more_than_6
prob_muldrotha_seven_land_hand = muldrotha_seven_land_hand/mana_more_than_6

# Since Muldrotha was NOT  Playable, initial hand was

prob_no_muldrotha_zero_land_hand = no_muldrotha_zero_land_hand/mana_less_than_6
prob_no_muldrotha_one_land_hand = no_muldrotha_one_land_hand/mana_less_than_6
prob_no_muldrotha_two_land_hand = no_muldrotha_two_land_hand/mana_less_than_6
prob_no_muldrotha_three_land_hand = no_muldrotha_three_land_hand/mana_less_than_6
prob_no_muldrotha_four_land_hand = no_muldrotha_four_land_hand/mana_less_than_6
prob_no_muldrotha_five_land_hand = no_muldrotha_five_land_hand/mana_less_than_6
prob_no_muldrotha_six_land_hand = no_muldrotha_six_land_hand/mana_less_than_6
prob_no_muldrotha_seven_land_hand = no_muldrotha_seven_land_hand/mana_less_than_6

print("----------------Simulation 3----------------")
print("Zero mana hand probability (with Muldrotha playble): ", prob_muldrotha_zero_land_hand)
print("One mana hand probability (with Muldrotha playble): ", prob_muldrotha_one_land_hand)
print("Two mana hand probability (with Muldrotha playble): ", prob_muldrotha_two_land_hand)
print("Three mana hand probability (with Muldrotha playble): ", prob_muldrotha_three_land_hand)
print("Four mana hand probability (with Muldrotha playble): ", prob_muldrotha_four_land_hand)
print("Five mana hand probability (with Muldrotha playble): ", prob_muldrotha_five_land_hand)
print("Six mana hand probability (with Muldrotha playble): ", prob_muldrotha_six_land_hand)
print("Seven mana hand probability (with Muldrotha playble): ", prob_muldrotha_seven_land_hand)

print("Zero mana hand probability (without Muldrotha playble): ", prob_no_muldrotha_zero_land_hand)
print("One mana hand probability (without Muldrotha playble): ", prob_no_muldrotha_one_land_hand)
print("Two mana hand probability (without Muldrotha playble): ", prob_no_muldrotha_two_land_hand)
print("Three mana hand probability (without Muldrotha playble): ", prob_no_muldrotha_three_land_hand)
print("Four mana hand probability (without Muldrotha playble): ", prob_no_muldrotha_four_land_hand)
print("Five mana hand probability (without Muldrotha playble): ", prob_no_muldrotha_five_land_hand)
print("Six mana hand probability (without Muldrotha playble): ", prob_no_muldrotha_six_land_hand)
print("Seven mana hand probability (without Muldrotha playble): ", prob_no_muldrotha_seven_land_hand)


#-------------------------------- 3 --------------------------------
# SIMULATION 3, BUT WITH TURN 4 

muldrotha_in_play = 0
no_muldrotha = 0

no_muldrotha_zero_land_hand = 0
no_muldrotha_one_land_hand = 0
no_muldrotha_two_land_hand = 0
no_muldrotha_three_land_hand = 0
no_muldrotha_four_land_hand = 0
no_muldrotha_five_land_hand = 0
no_muldrotha_six_land_hand = 0
no_muldrotha_seven_land_hand = 0

muldrotha_zero_land_hand = 0
muldrotha_one_land_hand = 0
muldrotha_two_land_hand = 0
muldrotha_three_land_hand = 0
muldrotha_four_land_hand = 0
muldrotha_five_land_hand = 0
muldrotha_six_land_hand = 0
muldrotha_seven_land_hand = 0

mana_more_than_6 = 0
mana_less_than_6 = 0

for hands in range(N):
    # shuffle the cards
    random.shuffle(Muldrotha_deck)
    LPM = [d[0] for d in Muldrotha_deck[0:10]].count('LPM')
    PM = [d[0] for d in Muldrotha_deck[0:10]].count('LPM')
    initial_hand_LPM = [d[0] for d in Muldrotha_deck[0:11]].count('LPM')
    initial_hand_PM = [d[0] for d in Muldrotha_deck[0:11]].count('PM')
        
    mana = LPM + PM
    initial_mana = initial_hand_PM + initial_hand_LPM

    if mana >= 6 :
        
        muldrotha_in_play += 1

        mana_more_than_6 += 1
        
        if initial_mana == 0:
                muldrotha_zero_land_hand+=1
        elif initial_mana == 1:
                muldrotha_one_land_hand+=1
        elif initial_mana == 2:
                muldrotha_two_land_hand+=1
        elif initial_mana == 3:
                muldrotha_three_land_hand+=1
        elif initial_mana == 4:
                muldrotha_four_land_hand+=1
        elif initial_mana == 5:
                muldrotha_five_land_hand+=1      
        elif initial_mana == 6:
                muldrotha_six_land_hand+=1        
        elif initial_mana == 7:
                muldrotha_seven_land_hand+=1
                
    else:
        
        no_muldrotha += 1

        mana_less_than_6 += 1
        
        if initial_mana == 0:
                no_muldrotha_zero_land_hand+=1
        elif initial_mana == 1:
                no_muldrotha_one_land_hand+=1
        elif initial_mana == 2:
                no_muldrotha_two_land_hand+=1
        elif initial_mana == 3:
                no_muldrotha_three_land_hand+=1
        elif initial_mana == 4:
                no_muldrotha_four_land_hand+=1
        elif initial_mana == 5:
                no_muldrotha_five_land_hand+=1      
        elif initial_mana == 6:
                no_muldrotha_six_land_hand+=1        
        elif initial_mana == 7:
                no_muldrotha_seven_land_hand+=1
        
# Muldrotha playable, turn 3
prob_muldrotha_in_play = muldrotha_in_play/N
prob_no_muldrotha = no_muldrotha/N

# Since Muldrotha was Playable, initial hand was

prob_muldrotha_zero_land_hand = muldrotha_zero_land_hand/mana_more_than_6
prob_muldrotha_one_land_hand = muldrotha_one_land_hand/mana_more_than_6
prob_muldrotha_two_land_hand = muldrotha_two_land_hand/mana_more_than_6
prob_muldrotha_three_land_hand = muldrotha_three_land_hand/mana_more_than_6
prob_muldrotha_four_land_hand = muldrotha_four_land_hand/mana_more_than_6
prob_muldrotha_five_land_hand = muldrotha_five_land_hand/mana_more_than_6
prob_muldrotha_six_land_hand = muldrotha_six_land_hand/mana_more_than_6
prob_muldrotha_seven_land_hand = muldrotha_seven_land_hand/mana_more_than_6

# Since Muldrotha was NOT  Playable, initial hand was

prob_no_muldrotha_zero_land_hand = no_muldrotha_zero_land_hand/mana_less_than_6
prob_no_muldrotha_one_land_hand = no_muldrotha_one_land_hand/mana_less_than_6
prob_no_muldrotha_two_land_hand = no_muldrotha_two_land_hand/mana_less_than_6
prob_no_muldrotha_three_land_hand = no_muldrotha_three_land_hand/mana_less_than_6
prob_no_muldrotha_four_land_hand = no_muldrotha_four_land_hand/mana_less_than_6
prob_no_muldrotha_five_land_hand = no_muldrotha_five_land_hand/mana_less_than_6 
prob_no_muldrotha_six_land_hand = no_muldrotha_six_land_hand/mana_less_than_6
prob_no_muldrotha_seven_land_hand = no_muldrotha_seven_land_hand/mana_less_than_6        

print("----------------Simulation 3, but turn 4----------------")
print("Zero mana hand probability (with Muldrotha playble): ", prob_muldrotha_zero_land_hand)
print("One mana hand probability (with Muldrotha playble): ", prob_muldrotha_one_land_hand)
print("Two mana hand probability (with Muldrotha playble): ", prob_muldrotha_two_land_hand)
print("Three mana hand probability (with Muldrotha playble): ", prob_muldrotha_three_land_hand)
print("Four mana hand probability (with Muldrotha playble): ", prob_muldrotha_four_land_hand)
print("Five mana hand probability (with Muldrotha playble): ", prob_muldrotha_five_land_hand)
print("Six mana hand probability (with Muldrotha playble): ", prob_muldrotha_six_land_hand)
print("Seven mana hand probability (with Muldrotha playble): ", prob_muldrotha_seven_land_hand)

print("Zero mana hand probability (without Muldrotha playble): ", prob_no_muldrotha_zero_land_hand)
print("One mana hand probability (without Muldrotha playble): ", prob_no_muldrotha_one_land_hand)
print("Two mana hand probability (without Muldrotha playble): ", prob_no_muldrotha_two_land_hand)
print("Three mana hand probability (without Muldrotha playble): ", prob_no_muldrotha_three_land_hand)
print("Four mana hand probability (without Muldrotha playble): ", prob_no_muldrotha_four_land_hand)
print("Five mana hand probability (without Muldrotha playble): ", prob_no_muldrotha_five_land_hand)
print("Six mana hand probability (without Muldrotha playble): ", prob_no_muldrotha_six_land_hand)
print("Seven mana hand probability (without Muldrotha playble): ", prob_no_muldrotha_seven_land_hand)

#-------------------------------- 3 --------------------------------
# SIMULATION 3, BUT WITH TURN 5

muldrotha_in_play = 0
no_muldrotha = 0

no_muldrotha_zero_land_hand = 0
no_muldrotha_one_land_hand = 0
no_muldrotha_two_land_hand = 0
no_muldrotha_three_land_hand = 0
no_muldrotha_four_land_hand = 0
no_muldrotha_five_land_hand = 0
no_muldrotha_six_land_hand = 0
no_muldrotha_seven_land_hand = 0

muldrotha_zero_land_hand = 0
muldrotha_one_land_hand = 0
muldrotha_two_land_hand = 0
muldrotha_three_land_hand = 0
muldrotha_four_land_hand = 0
muldrotha_five_land_hand = 0
muldrotha_six_land_hand = 0
muldrotha_seven_land_hand = 0

mana_more_than_6 = 0
mana_less_than_6 = 0

for hands in range(N):
    # shuffle the cards
    random.shuffle(Muldrotha_deck)
    LPM = [d[0] for d in Muldrotha_deck[0:10]].count('LPM')
    PM = [d[0] for d in Muldrotha_deck[0:10]].count('LPM')
    initial_hand_LPM = [d[0] for d in Muldrotha_deck[0:12]].count('LPM')
    initial_hand_PM = [d[0] for d in Muldrotha_deck[0:12]].count('PM')
        
    mana = LPM + PM
    initial_mana = initial_hand_PM + initial_hand_LPM

    if mana >= 6 :
        
        muldrotha_in_play += 1
        
        mana_more_than_6 += 1
        
        if initial_mana == 0:
                muldrotha_zero_land_hand+=1
        elif initial_mana == 1:
                muldrotha_one_land_hand+=1
        elif initial_mana == 2:
                muldrotha_two_land_hand+=1
        elif initial_mana == 3:
                muldrotha_three_land_hand+=1
        elif initial_mana == 4:
                muldrotha_four_land_hand+=1
        elif initial_mana == 5:
                muldrotha_five_land_hand+=1      
        elif initial_mana == 6:
                muldrotha_six_land_hand+=1        
        elif initial_mana == 7:
                muldrotha_seven_land_hand+=1
                
    else:
        
        no_muldrotha += 1

        mana_less_than_6 += 1
        
        if initial_mana == 0:
                no_muldrotha_zero_land_hand+=1
        elif initial_mana == 1:
                no_muldrotha_one_land_hand+=1
        elif initial_mana == 2:
                no_muldrotha_two_land_hand+=1
        elif initial_mana == 3:
                no_muldrotha_three_land_hand+=1
        elif initial_mana == 4:
                no_muldrotha_four_land_hand+=1
        elif initial_mana == 5:
                no_muldrotha_five_land_hand+=1      
        elif initial_mana == 6:
                no_muldrotha_six_land_hand+=1        
        elif initial_mana == 7:
                no_muldrotha_seven_land_hand+=1
        
# Muldrotha playable, turn 3
prob_muldrotha_in_play = muldrotha_in_play/N
prob_no_muldrotha = no_muldrotha/N

# Since Muldrotha was Playable, initial hand was

prob_muldrotha_zero_land_hand = muldrotha_zero_land_hand/mana_more_than_6
prob_muldrotha_one_land_hand = muldrotha_one_land_hand/mana_more_than_6
prob_muldrotha_two_land_hand = muldrotha_two_land_hand/mana_more_than_6
prob_muldrotha_three_land_hand = muldrotha_three_land_hand/mana_more_than_6
prob_muldrotha_four_land_hand = muldrotha_four_land_hand/mana_more_than_6
prob_muldrotha_five_land_hand = muldrotha_five_land_hand/mana_more_than_6
prob_muldrotha_six_land_hand = muldrotha_six_land_hand/mana_more_than_6
prob_muldrotha_seven_land_hand = muldrotha_seven_land_hand/mana_more_than_6

# Since Muldrotha was NOT  Playable, initial hand was

prob_no_muldrotha_zero_land_hand = no_muldrotha_zero_land_hand/mana_less_than_6
prob_no_muldrotha_one_land_hand = no_muldrotha_one_land_hand/mana_less_than_6
prob_no_muldrotha_two_land_hand = no_muldrotha_two_land_hand/mana_less_than_6
prob_no_muldrotha_three_land_hand = no_muldrotha_three_land_hand/mana_less_than_6
prob_no_muldrotha_four_land_hand = no_muldrotha_four_land_hand/mana_less_than_6
prob_no_muldrotha_five_land_hand = no_muldrotha_five_land_hand/mana_less_than_6
prob_no_muldrotha_six_land_hand = no_muldrotha_six_land_hand/mana_less_than_6
prob_no_muldrotha_seven_land_hand = no_muldrotha_seven_land_hand/mana_less_than_6
        
print("----------------Simulation 3, but turn 5----------------")
print("Zero mana hand probability (with Muldrotha playble): ", prob_muldrotha_zero_land_hand)
print("One mana hand probability (with Muldrotha playble): ", prob_muldrotha_one_land_hand)
print("Two mana hand probability (with Muldrotha playble): ", prob_muldrotha_two_land_hand)
print("Three mana hand probability (with Muldrotha playble): ", prob_muldrotha_three_land_hand)
print("Four mana hand probability (with Muldrotha playble): ", prob_muldrotha_four_land_hand)
print("Five mana hand probability (with Muldrotha playble): ", prob_muldrotha_five_land_hand)
print("Six mana hand probability (with Muldrotha playble): ", prob_muldrotha_six_land_hand)
print("Seven mana hand probability (with Muldrotha playble): ", prob_muldrotha_seven_land_hand)

print("Zero mana hand probability (without Muldrotha playble): ", prob_no_muldrotha_zero_land_hand)
print("One mana hand probability (without Muldrotha playble): ", prob_no_muldrotha_one_land_hand)
print("Two mana hand probability (without Muldrotha playble): ", prob_no_muldrotha_two_land_hand)
print("Three mana hand probability (without Muldrotha playble): ", prob_no_muldrotha_three_land_hand)
print("Four mana hand probability (without Muldrotha playble): ", prob_no_muldrotha_four_land_hand)
print("Five mana hand probability (without Muldrotha playble): ", prob_no_muldrotha_five_land_hand)
print("Six mana hand probability (without Muldrotha playble): ", prob_no_muldrotha_six_land_hand)
print("Seven mana hand probability (without Muldrotha playble): ", prob_no_muldrotha_seven_land_hand)
        
        
#-------------------------------- 3 --------------------------------
# SIMULATION 3, BUT WITH TURN 6 

muldrotha_in_play = 0
no_muldrotha = 0

no_muldrotha_zero_land_hand = 0
no_muldrotha_one_land_hand = 0
no_muldrotha_two_land_hand = 0
no_muldrotha_three_land_hand = 0
no_muldrotha_four_land_hand = 0
no_muldrotha_five_land_hand = 0
no_muldrotha_six_land_hand = 0
no_muldrotha_seven_land_hand = 0

muldrotha_zero_land_hand = 0
muldrotha_one_land_hand = 0
muldrotha_two_land_hand = 0
muldrotha_three_land_hand = 0
muldrotha_four_land_hand = 0
muldrotha_five_land_hand = 0
muldrotha_six_land_hand = 0
muldrotha_seven_land_hand = 0

mana_more_than_6 = 0
mana_less_than_6 = 0

for hands in range(N):
    # shuffle the cards
    random.shuffle(Muldrotha_deck)
    LPM = [d[0] for d in Muldrotha_deck[0:10]].count('LPM')
    PM = [d[0] for d in Muldrotha_deck[0:10]].count('LPM')
    initial_hand_LPM = [d[0] for d in Muldrotha_deck[0:13]].count('LPM')
    initial_hand_PM = [d[0] for d in Muldrotha_deck[0:13]].count('PM')
        
    mana = LPM + PM
    initial_mana = initial_hand_PM + initial_hand_LPM

    if mana >= 6 :
        
        muldrotha_in_play += 1

        mana_more_than_6 += 1
        
        if initial_mana == 0:
                muldrotha_zero_land_hand+=1
        elif initial_mana == 1:
                muldrotha_one_land_hand+=1
        elif initial_mana == 2:
                muldrotha_two_land_hand+=1
        elif initial_mana == 3:
                muldrotha_three_land_hand+=1
        elif initial_mana == 4:
                muldrotha_four_land_hand+=1
        elif initial_mana == 5:
                muldrotha_five_land_hand+=1      
        elif initial_mana == 6:
                muldrotha_six_land_hand+=1        
        elif initial_mana == 7:
                muldrotha_seven_land_hand+=1
                
    else:
        
        no_muldrotha += 1

        mana_less_than_6 += 1
        
        if initial_mana == 0:
                no_muldrotha_zero_land_hand+=1
        elif initial_mana == 1:
                no_muldrotha_one_land_hand+=1
        elif initial_mana == 2:
                no_muldrotha_two_land_hand+=1
        elif initial_mana == 3:
                no_muldrotha_three_land_hand+=1
        elif initial_mana == 4:
                no_muldrotha_four_land_hand+=1
        elif initial_mana == 5:
                no_muldrotha_five_land_hand+=1      
        elif initial_mana == 6:
                no_muldrotha_six_land_hand+=1        
        elif initial_mana == 7:
                no_muldrotha_seven_land_hand+=1
        
# Muldrotha playable, turn 3
prob_muldrotha_in_play = muldrotha_in_play/N
prob_no_muldrotha = no_muldrotha/N

# Since Muldrotha was Playable, initial hand was

prob_muldrotha_zero_land_hand = muldrotha_zero_land_hand/mana_more_than_6
prob_muldrotha_one_land_hand = muldrotha_one_land_hand/mana_more_than_6
prob_muldrotha_two_land_hand = muldrotha_two_land_hand/mana_more_than_6
prob_muldrotha_three_land_hand = muldrotha_three_land_hand/mana_more_than_6
prob_muldrotha_four_land_hand = muldrotha_four_land_hand/mana_more_than_6
prob_muldrotha_five_land_hand = muldrotha_five_land_hand/mana_more_than_6
prob_muldrotha_six_land_hand = muldrotha_six_land_hand/mana_more_than_6
prob_muldrotha_seven_land_hand = muldrotha_seven_land_hand/mana_more_than_6

# Since Muldrotha was NOT  Playable, initial hand was

prob_no_muldrotha_zero_land_hand = no_muldrotha_zero_land_hand/mana_less_than_6
prob_no_muldrotha_one_land_hand = no_muldrotha_one_land_hand/mana_less_than_6
prob_no_muldrotha_two_land_hand = no_muldrotha_two_land_hand/mana_less_than_6
prob_no_muldrotha_three_land_hand = no_muldrotha_three_land_hand/mana_less_than_6
prob_no_muldrotha_four_land_hand = no_muldrotha_four_land_hand/mana_less_than_6
prob_no_muldrotha_five_land_hand = no_muldrotha_five_land_hand/mana_less_than_6
prob_no_muldrotha_six_land_hand = no_muldrotha_six_land_hand/mana_less_than_6
prob_no_muldrotha_seven_land_hand = no_muldrotha_seven_land_hand/mana_less_than_6

print("----------------Simulation 3, but turn 6----------------")
print("Zero mana hand probability (with Muldrotha playble): ", prob_muldrotha_zero_land_hand)
print("One mana hand probability (with Muldrotha playble): ", prob_muldrotha_one_land_hand)
print("Two mana hand probability (with Muldrotha playble): ", prob_muldrotha_two_land_hand)
print("Three mana hand probability (with Muldrotha playble): ", prob_muldrotha_three_land_hand)
print("Four mana hand probability (with Muldrotha playble): ", prob_muldrotha_four_land_hand)
print("Five mana hand probability (with Muldrotha playble): ", prob_muldrotha_five_land_hand)
print("Six mana hand probability (with Muldrotha playble): ", prob_muldrotha_six_land_hand)
print("Seven mana hand probability (with Muldrotha playble): ", prob_muldrotha_seven_land_hand)

print("Zero mana hand probability (without Muldrotha playble): ", prob_no_muldrotha_zero_land_hand)
print("One mana hand probability (without Muldrotha playble): ", prob_no_muldrotha_one_land_hand)
print("Two mana hand probability (without Muldrotha playble): ", prob_no_muldrotha_two_land_hand)
print("Three mana hand probability (without Muldrotha playble): ", prob_no_muldrotha_three_land_hand)
print("Four mana hand probability (without Muldrotha playble): ", prob_no_muldrotha_four_land_hand)
print("Five mana hand probability (without Muldrotha playble): ", prob_no_muldrotha_five_land_hand)
print("Six mana hand probability (without Muldrotha playble): ", prob_no_muldrotha_six_land_hand)
print("Seven mana hand probability (without Muldrotha playble): ", prob_no_muldrotha_seven_land_hand)
        
#-------------------------------- 3 --------------------------------
# SIMULATION 3, BUT WITH TURN 7 

muldrotha_in_play = 0
no_muldrotha = 0

no_muldrotha_zero_land_hand = 0
no_muldrotha_one_land_hand = 0
no_muldrotha_two_land_hand = 0
no_muldrotha_three_land_hand = 0
no_muldrotha_four_land_hand = 0
no_muldrotha_five_land_hand = 0
no_muldrotha_six_land_hand = 0
no_muldrotha_seven_land_hand = 0

muldrotha_zero_land_hand = 0
muldrotha_one_land_hand = 0
muldrotha_two_land_hand = 0
muldrotha_three_land_hand = 0
muldrotha_four_land_hand = 0
muldrotha_five_land_hand = 0
muldrotha_six_land_hand = 0
muldrotha_seven_land_hand = 0

mana_more_than_6 = 0
mana_less_than_6 = 0

for hands in range(N):
    # shuffle the cards
    random.shuffle(Muldrotha_deck)
    LPM = [d[0] for d in Muldrotha_deck[0:10]].count('LPM')
    PM = [d[0] for d in Muldrotha_deck[0:10]].count('LPM')
    initial_hand_LPM = [d[0] for d in Muldrotha_deck[0:14]].count('LPM')
    initial_hand_PM = [d[0] for d in Muldrotha_deck[0:14]].count('PM')
        
    mana = LPM + PM
    initial_mana = initial_hand_PM + initial_hand_LPM

    if mana >= 6 :
        
        muldrotha_in_play += 1
        
        mana_more_than_6 += 1

        if initial_mana == 0:
                muldrotha_zero_land_hand+=1
        elif initial_mana == 1:
                muldrotha_one_land_hand+=1
        elif initial_mana == 2:
                muldrotha_two_land_hand+=1
        elif initial_mana == 3:
                muldrotha_three_land_hand+=1
        elif initial_mana == 4:
                muldrotha_four_land_hand+=1
        elif initial_mana == 5:
                muldrotha_five_land_hand+=1      
        elif initial_mana == 6:
                muldrotha_six_land_hand+=1        
        elif initial_mana == 7:
                muldrotha_seven_land_hand+=1
                
    else:
        
        no_muldrotha += 1

        mana_less_than_6 += 1
        
        if initial_mana == 0:
                no_muldrotha_zero_land_hand+=1
        elif initial_mana == 1:
                no_muldrotha_one_land_hand+=1
        elif initial_mana == 2:
                no_muldrotha_two_land_hand+=1
        elif initial_mana == 3:
                no_muldrotha_three_land_hand+=1
        elif initial_mana == 4:
                no_muldrotha_four_land_hand+=1
        elif initial_mana == 5:
                no_muldrotha_five_land_hand+=1      
        elif initial_mana == 6:
                no_muldrotha_six_land_hand+=1        
        elif initial_mana == 7:
                no_muldrotha_seven_land_hand+=1
        
# Muldrotha playable, turn 3
prob_muldrotha_in_play = muldrotha_in_play/N
prob_no_muldrotha = no_muldrotha/N

# Since Muldrotha was Playable, initial hand was

prob_muldrotha_zero_land_hand = muldrotha_zero_land_hand/mana_more_than_6
prob_muldrotha_one_land_hand = muldrotha_one_land_hand/mana_more_than_6
prob_muldrotha_two_land_hand = muldrotha_two_land_hand/mana_more_than_6
prob_muldrotha_three_land_hand = muldrotha_three_land_hand/mana_more_than_6
prob_muldrotha_four_land_hand = muldrotha_four_land_hand/mana_more_than_6
prob_muldrotha_five_land_hand = muldrotha_five_land_hand/mana_more_than_6
prob_muldrotha_six_land_hand = muldrotha_six_land_hand/mana_more_than_6
prob_muldrotha_seven_land_hand = muldrotha_seven_land_hand/mana_more_than_6

# Since Muldrotha was NOT  Playable, initial hand was

prob_no_muldrotha_zero_land_hand = no_muldrotha_zero_land_hand/mana_less_than_6
prob_no_muldrotha_one_land_hand = no_muldrotha_one_land_hand/mana_less_than_6
prob_no_muldrotha_two_land_hand = no_muldrotha_two_land_hand/mana_less_than_6
prob_no_muldrotha_three_land_hand = no_muldrotha_three_land_hand/mana_less_than_6
prob_no_muldrotha_four_land_hand = no_muldrotha_four_land_hand/mana_less_than_6
prob_no_muldrotha_five_land_hand = no_muldrotha_five_land_hand/mana_less_than_6
prob_no_muldrotha_six_land_hand = no_muldrotha_six_land_hand/mana_less_than_6
prob_no_muldrotha_seven_land_hand = no_muldrotha_seven_land_hand/mana_less_than_6

print("----------------Simulation 3, but turn 7----------------")
print("Zero mana hand probability (with Muldrotha playble): ", prob_muldrotha_zero_land_hand)
print("One mana hand probability (with Muldrotha playble): ", prob_muldrotha_one_land_hand)
print("Two mana hand probability (with Muldrotha playble): ", prob_muldrotha_two_land_hand)
print("Three mana hand probability (with Muldrotha playble): ", prob_muldrotha_three_land_hand)
print("Four mana hand probability (with Muldrotha playble): ", prob_muldrotha_four_land_hand)
print("Five mana hand probability (with Muldrotha playble): ", prob_muldrotha_five_land_hand)
print("Six mana hand probability (with Muldrotha playble): ", prob_muldrotha_six_land_hand)
print("Seven mana hand probability (with Muldrotha playble): ", prob_muldrotha_seven_land_hand)

print("Zero mana hand probability (without Muldrotha playble): ", prob_no_muldrotha_zero_land_hand)
print("One mana hand probability (without Muldrotha playble): ", prob_no_muldrotha_one_land_hand)
print("Two mana hand probability (without Muldrotha playble): ", prob_no_muldrotha_two_land_hand)
print("Three mana hand probability (without Muldrotha playble): ", prob_no_muldrotha_three_land_hand)
print("Four mana hand probability (without Muldrotha playble): ", prob_no_muldrotha_four_land_hand)
print("Five mana hand probability (without Muldrotha playble): ", prob_no_muldrotha_five_land_hand)
print("Six mana hand probability (without Muldrotha playble): ", prob_no_muldrotha_six_land_hand)
print("Seven mana hand probability (without Muldrotha playble): ", prob_no_muldrotha_seven_land_hand)


#-------------------------------- 3 --------------------------------
# SIMULATION 3, BUT WITH TURN 8 

muldrotha_in_play = 0
no_muldrotha = 0

no_muldrotha_zero_land_hand = 0
no_muldrotha_one_land_hand = 0
no_muldrotha_two_land_hand = 0
no_muldrotha_three_land_hand = 0
no_muldrotha_four_land_hand = 0
no_muldrotha_five_land_hand = 0
no_muldrotha_six_land_hand = 0
no_muldrotha_seven_land_hand = 0

muldrotha_zero_land_hand = 0
muldrotha_one_land_hand = 0
muldrotha_two_land_hand = 0
muldrotha_three_land_hand = 0
muldrotha_four_land_hand = 0
muldrotha_five_land_hand = 0
muldrotha_six_land_hand = 0
muldrotha_seven_land_hand = 0

mana_more_than_6 = 0
mana_less_than_6 = 0

for hands in range(N):
    # shuffle the cards
    random.shuffle(Muldrotha_deck)
    LPM = [d[0] for d in Muldrotha_deck[0:10]].count('LPM')
    PM = [d[0] for d in Muldrotha_deck[0:10]].count('LPM')
    initial_hand_LPM = [d[0] for d in Muldrotha_deck[0:15]].count('LPM')
    initial_hand_PM = [d[0] for d in Muldrotha_deck[0:15]].count('PM')
        
    mana = LPM + PM
    initial_mana = initial_hand_PM + initial_hand_LPM

    if mana >= 6 :

        mana_more_than_6 += 1 
        
        muldrotha_in_play += 1
        
        if initial_mana == 0:
                muldrotha_zero_land_hand+=1
        elif initial_mana == 1:
                muldrotha_one_land_hand+=1
        elif initial_mana == 2:
                muldrotha_two_land_hand+=1
        elif initial_mana == 3:
                muldrotha_three_land_hand+=1
        elif initial_mana == 4:
                muldrotha_four_land_hand+=1
        elif initial_mana == 5:
                muldrotha_five_land_hand+=1      
        elif initial_mana == 6:
                muldrotha_six_land_hand+=1        
        elif initial_mana == 7:
                muldrotha_seven_land_hand+=1
                
    else:
        
        no_muldrotha += 1

        mana_less_than_6 += 1
        
        if initial_mana == 0:
                no_muldrotha_zero_land_hand+=1
        elif initial_mana == 1:
                no_muldrotha_one_land_hand+=1
        elif initial_mana == 2:
                no_muldrotha_two_land_hand+=1
        elif initial_mana == 3:
                no_muldrotha_three_land_hand+=1
        elif initial_mana == 4:
                no_muldrotha_four_land_hand+=1
        elif initial_mana == 5:
                no_muldrotha_five_land_hand+=1      
        elif initial_mana == 6:
                no_muldrotha_six_land_hand+=1        
        elif initial_mana == 7:
                no_muldrotha_seven_land_hand+=1
        
# Muldrotha playable, turn 3
prob_muldrotha_in_play = muldrotha_in_play/N
prob_no_muldrotha = no_muldrotha/N

# Since Muldrotha was Playable, initial hand was

prob_muldrotha_zero_land_hand = muldrotha_zero_land_hand/mana_more_than_6
prob_muldrotha_one_land_hand = muldrotha_one_land_hand/mana_more_than_6
prob_muldrotha_two_land_hand = muldrotha_two_land_hand/mana_more_than_6
prob_muldrotha_three_land_hand = muldrotha_three_land_hand/mana_more_than_6
prob_muldrotha_four_land_hand = muldrotha_four_land_hand/mana_more_than_6
prob_muldrotha_five_land_hand = muldrotha_five_land_hand/mana_more_than_6              
prob_muldrotha_six_land_hand = muldrotha_six_land_hand/mana_more_than_6       
prob_muldrotha_seven_land_hand = muldrotha_seven_land_hand/mana_more_than_6     

# Since Muldrotha was NOT  Playable, initial hand was

prob_no_muldrotha_zero_land_hand = no_muldrotha_zero_land_hand/mana_less_than_6
prob_no_muldrotha_one_land_hand = no_muldrotha_one_land_hand/mana_less_than_6
prob_no_muldrotha_two_land_hand = no_muldrotha_two_land_hand/mana_less_than_6
prob_no_muldrotha_three_land_hand = no_muldrotha_three_land_hand/mana_less_than_6
prob_no_muldrotha_four_land_hand = no_muldrotha_four_land_hand/mana_less_than_6
prob_no_muldrotha_five_land_hand = no_muldrotha_five_land_hand/mana_less_than_6              
prob_no_muldrotha_six_land_hand = no_muldrotha_six_land_hand/mana_less_than_6       
prob_no_muldrotha_seven_land_hand = no_muldrotha_seven_land_hand/mana_less_than_6 

print("----------------Simulation 3, but turn 8----------------")
print("Zero mana hand probability (with Muldrotha playble): ", prob_muldrotha_zero_land_hand)
print("One mana hand probability (with Muldrotha playble): ", prob_muldrotha_one_land_hand)
print("Two mana hand probability (with Muldrotha playble): ", prob_muldrotha_two_land_hand)
print("Three mana hand probability (with Muldrotha playble): ", prob_muldrotha_three_land_hand)
print("Four mana hand probability (with Muldrotha playble): ", prob_muldrotha_four_land_hand)
print("Five mana hand probability (with Muldrotha playble): ", prob_muldrotha_five_land_hand)
print("Six mana hand probability (with Muldrotha playble): ", prob_muldrotha_six_land_hand)
print("Seven mana hand probability (with Muldrotha playble): ", prob_muldrotha_seven_land_hand)

print("Zero mana hand probability (without Muldrotha playble): ", prob_no_muldrotha_zero_land_hand)
print("One mana hand probability (without Muldrotha playble): ", prob_no_muldrotha_one_land_hand)
print("Two mana hand probability (without Muldrotha playble): ", prob_no_muldrotha_two_land_hand)
print("Three mana hand probability (without Muldrotha playble): ", prob_no_muldrotha_three_land_hand)
print("Four mana hand probability (without Muldrotha playble): ", prob_no_muldrotha_four_land_hand)
print("Five mana hand probability (without Muldrotha playble): ", prob_no_muldrotha_five_land_hand)
print("Six mana hand probability (without Muldrotha playble): ", prob_no_muldrotha_six_land_hand)
print("Seven mana hand probability (without Muldrotha playble): ", prob_no_muldrotha_seven_land_hand)
