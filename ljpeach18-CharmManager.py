#Liam Peachey
#ljpeach18-CharmManager.py
class Charm:
    '''
    The Charm object represents a single charm.

    Parameters
    ----------
    rarity : int
        The rarity of the charm.

    skill1 : str
        The name of the charm's first skill

    skill1Points : int
        The number of skill points towards skill1 that the charm has

    skill2 : str
        The name of the charm's second skill

    skill2Points : int
        The number of skill points towards skill2 that the charm has

    slots : int
        The number of decoration slots the charm has

    Attributes
    ----------
    rarity : int
        The rarity of the charm

    skill1 : tuple
        The information for skill 1. First index is the skill name (string), and the second is the skill points (int).

    skill2 : tuple
        The information for skill 2. First index is the skill name (string), and the second is the skill points (int).

    slots : int
        The number of decoration slots the charm has
    '''
    def __init__(self, rarity, skill1, s1Points, skill2, s2points, slots):
        self.rarity = rarity
        self.skill1 = skill1,s1Points
        self.skill2 = skill2,s2points
        self.slots = slots

    def csvReadyString(self):
        '''
        This function converts the charm data into a string that can be easily written out to a csv file.

        Returns
        -------
        str
            A string in CSV format (comma separated).
        '''
        skill2Points = str(self.skill2[1])
        if skill2Points == "0":
            skill2Points = "-"
            #return rarity,skill1,skill1 points,skill2,skill2 points,slots
        return str(self.rarity)+","+self.skill1[0]+","+str(self.skill1[1])+","+self.skill2[0]+","+skill2Points+","+str(self.slots)

    def __str__(self):
        skill2Points = str(self.skill2[1])
        if skill2Points == "0":
            skill2Points = "-"
        #formatted = skill1: skill1 points | skill2: skill2 points |
        formatted = self.skill1[0] + ": " + str(self.skill1[1]) + " | " + self.skill2[0] + ": " + skill2Points + " | "
        if self.slots == 0:
            return formatted + "---"
        return formatted + "O"*self.slots

    def __eq__(self,other):
        return self.rarity == other.rarity and self.skill1 == other.skill1 and self.skill2 == other.skill2 and self.slots == other.slots

class CharmManager:
    '''
    A charm manager object reads saved charm data in from a CSV file, organizes the charms into the standard order, and then allows for a number of operations to make charm management easier.

    Attributes
    ----------
    charmList : list
        A list of all charms. Stores charms.

    bestDict : dict
        A dictionary of best items. Keys are the skill names, items are the charms.

    skillDict : dict
        A dictionary containing all skills that charms can contribute to.
        Format for skillDict elements:
            "skill name" :
            (
                [Order in skill list. Not sorted alphabetically, so this is needed.],
                ([points from one slot], [points from two slots], [points from three slots]),
                ([max skill1 points], [max skill2 points], [points needed for highest tier of activation])
            )
    '''
    def __init__(self):
        self.charmList = []
        self.bestDict = {}
        #Format for skillDict elements: "skill name" : (Order in skill list. Not sorted alphabetically, so this is needed., (points from one slot, points from two slots, points from three slots), (max skill1 points, max skill2 points, points needed for highest tier of activation))
        self.skillDict={
                "Poison" : (1, (1,3,4), (5,7,10)),
                "Paralysis" : (2, (1,3,4), (5,7,10)),
                "Sleep" : (3, (1,3,4), (5,7,10)),
                "Stun" : (4, (2,4,6), (8,13,15)),
                "Hearing" : (5, (1,2,4), (7,5,15)),
                "Wind Res" : (6, (1,3,4), (10,7,15)),
                "Tremor Res" : (7, (2,4,6), (7,8,10)),
                "Bind Res" : (8, (2,4,6), (7,8,10)),
                "Heat Res" : (9, (2,4,6), (10,10,10)),
                "Cold Res" : (10, (2,4,6), (10,10,10)),
                "Coldblooded" : (11, (1,2,4), (7,0,10)),
                "Hotblooded" : (12, (1,2,4), (7,0,10)),
                "Anti Theft" : (13, (2,4,6), (10,10,10)),
                "Def Lock" : (14, (2,4,6), (7,8,10)),
                "Frenzy Res" : (15, (1,2,5), (7,5,10)),
                "Biology" : (16, (2,4,6), (10,5,15)),
                "Bleeding" : (17, (2,4,6), (5,10,10)),
                "Attack" : (18, (1,3,5), (4,10,20)),
                "Defense" : (19, (1,3,4), (4,13,20)),
                "Health" : (20, (2,4,6), (8,13,15)),
                "Fire Res" : (21, (2,4,6), (6,13,15)),
                "Water Res" : (22, (2,4,6), (6,13,15)),
                "Thunder Res" : (23, (2,4,6), (6,13,15)),
                "Ice Res" : (24, (2,4,6), (6,13,15)),
                "Dragon Res" : (25, (2,4,6), (6,13,15)),
                "Blight Res" : (26, (1,2,4), (7,7,10)),
                "Fire Atk" : (27, (1,3,4), (7,13,15)),
                "Water Atk" : (28, (1,3,4), (7,13,15)),
                "Thunder Atk" : (29, (1,3,4), (7,13,15)),
                "Ice Atk" : (30, (1,3,4), (7,13,15)),
                "Dragon Atk" : (31, (1,3,4), (7,13,15)),
                "Elemental" : (32, (1,2,4), (7,0,10)),
                "Status" : (33, (1,3,4), (7,7,15)),
                "Sharpener" : (34, (2,4,6), (4,10,10)),
                "Handicraft" : (35, (1,2,4), (0,5,15)),
                "Sharpness" : (36, (1,2,4), (7,7,10)),
                "Fencing" : (37, (1,2,4), (7,7,10)),
                "Grinder" : (38, (1,2,4), (5,5,10)),
                "Blunt" : (39, (1,3,4), (6,0,10)),
                "Crit Draw" : (40, (1,3,4), (5,5,10)),
                "Punish Draw" : (41, (1,2,4), (5,8,10)),
                "Sheathing" : (42, (1,3,4), (10,7,10)),
                "Sheathe Sharpen" : (43, (2,4,6), (10,3,10)),
                "Bladescale" : (44, (1,2,4), (0,3,10)),
                "Reload Spd" : (45, (1,3,4), (7,7,20)),
                "Recoil" : (46, (1,2,4), (6,7,20)),
                "Precision" : (47, (2,4,6), (6,10,15)),
                "Normal Up" : (48, (1,2,4), (6,5,10)),
                "Pierce Up" : (49, (1,2,4), (6,5,10)),
                "Pellet Up" : (50, (1,2,4), (6,5,10)),
                "Heavy Up" : (51, (1,2,4), (6,5,10)),
                "Normal S" : (52, (1,3,4), (6,8,10)),
                "Pierce S" : (53, (2,4,6), (10,10,15)),
                "Pellet S" : (54, (2,4,6), (10,10,15)),
                "Crag S" : (55, (2,4,6), (10,10,15)),
                "Clust S" : (56, (1,2,4), (10,10,15)),
                "Poison C" : (57, (2,4,6), (8,10,10)),
                "Para C" : (58, (1,3,4), (8,10,10)),
                "Sleep C" : (59, (2,4,6), (8,10,10)),
                "Power C" : (60, (1,3,4), (8,12,15)),
                "Elem C" : (61, (1,3,4), (8,12,15)),
                "Close Range C" : (62, (2,4,6), (8,10,10)),
                "Exhaust C" : (63, (2,4,6), (10,10,10)),
                "Blast C" : (64, (2,4,6), (10,10,10)),
                "Rapid Fire" : (65, (1,2,4), (5,5,10)),
                "Dead Eye" : (66, (1,3,4), (5,5,10)),
                "Loading" : (67, (1,2,4), (5,5,10)),
                "Haphazard" : (68, (2,4,6), (5,10,10)),
                "Ammo Saver" : (69, (1,3,4), (7,7,10)),
                "Expert" : (70, (1,3,5), (4,10,20)),
                "Tenderizer" : (71, (1,2,4), (6,5,10)),
                "Chain Crit" : (72, (1,2,4), (5,3,10)),
                "Crit Status" : (73, (1,3,4), (6,5,10)),
                "Crit Element" : (74, (1,3,4), (6,5,10)),
                "Critical Up" : (75, (1,2,4), (0,5,10)),
                "Negative Crit" : (76, (1,2,4), (0,3,10)),
                "Fast Charge" : (77, (1,2,4), (6,5,10)),
                "Stamina" : (78, (1,2,4), (6,5,10)),
                "Constitution" : (79, (1,3,4), (7,5,10)),
                "Stam Recov" : (80, (1,3,4), (7,5,10)),
                "Distance Runner" : (81, (1,3,4), (6,5,10)),
                "Evasion" : (82, (1,3,4), (6,5,15)),
                "Evade Dist" : (83, (1,2,4), (6,5,10)),
                "Bubble" : (84, (1,2,4), (5,3,10)),
                "Guard" : (85, (1,3,4), (7,5,15)),
                "Guard Up" : (86, (1,3,4), (7,5,10)),
                "KO" : (87, (1,3,4), (10,10,10)),
                "Stam Drain" : (88, (1,3,4), (10,10,10)),
                "Maestro" : (89, (2,4,6), (6,10,10)),
                "Artillery" : (90, (2,4,6), (6,10,15)),
                "Destroyer" : (91, (1,2,4), (6,5,10)),
                "Bomb Boost" : (92, (2,4,6), (6,10,10)),
                "Gloves Off" : (93, (1,3,4), (6,5,15)),
                "Spirit" : (94, (1,3,4), (5,3,15)),
                "Unscathed" : (95, (1,3,4), (5,3,10)),
                "Chance" : (96, (1,2,4), (5,3,10)),
                "Dragon Spirit" : (97, (1,2,4), (0,3,10)),
                "Potential" : (98, (1,3,4), (6,5,15)),
                "Survivor" : (99, (1,3,4), (5,5,10)),
                "Furor" : (100, (1,3,4), (6,5,10)),
                "Crisis" : (101, (1,3,4), (6,5,10)),
                "Guts" : (102, (1,3,4), (5,3,10)),
                "Sense" : (103, (2,4,6), (8,10,10)),
                "Team Player" : (104, (2,4,6), (7,10,10)),
                "Team Leader" : (105, (1,3,4), (7,10,10)),
                "Mounting" : (106, (2,4,6), (10,10,10)),
                "Vault" : (107, (2,4,6), (6,5,10)),
                "Insight" : (108, (1,2,4), (5,3,10)),
                "Endurance" : (109, (2,4,6), (7,7,10)),
                "Prolong SP" : (110, (1,3,4), (7,7,10)),
                "Psychic" : (111, (2,4,6), (8,12,15)),
                "Perception" : (112, (2,4,6), (8,10,10)),
                "Ranger" : (113, (2,4,6), (8,10,10)),
                "Transporter" : (114, (2,4,6), (8,10,10)),
                "Protection" : (115, (2,4,6), (7,10,10)),
                "Hero Shield" : (116, (1,2,4), (5,3,10)),
                "Rec Level" : (117, (1,3,4), (7,5,10)),
                "Rec Speed" : (118, (1,3,4), (7,12,15)),
                "Lasting Power" : (119, (2,4,6), (8,10,10)),
                "Wide Range" : (120, (1,3,4), (8,12,15)),
                "Hunger" : (121, (2,4,6), (8,10,15)),
                "Gluttony" : (122, (2,4,6), (10,13,15)),
                "Eating" : (123, (1,2,4), (6,5,15)),
                "Light Eater" : (124, (2,4,6), (7,7,10)),
                "Carnivore" : (125, (2,4,6), (5,5,10)),
                "Mycology" : (126, (2,4,6), (0,5,10)),
                "Botany" : (127, (2,4,6), (8,10,15)),
                "Combo Rate" : (128, (2,4,6), (10,13,15)),
                "Combo Plus" : (129, (2,4,6), (8,10,10)),
                "Speed Setup" : (130, (2,4,6), (8,10,10)),
                "Gathering" : (131, (2,4,6), (10,13,15)),
                "Honey" : (132, (2,4,6), (8,10,10)),
                "Charmer" : (133, (1,2,4), (7,10,15)),
                "Whim" : (134, (2,4,6), (10,13,15)),
                "Fate" : (135, (1,2,4), (0,7,20)),
                "Carving" : (136, (1,2,4), (0,5,15)),
                "Capturer" : (137, (1,2,4), (0,7,15)),
                "Redhelm" : (138, (0,0,0), (0,3,10)),
                "Snowbaron" : (139, (0,0,0), (0,3,10)),
                "Stonefist" : (140, (0,0,0), (0,3,10)),
                "Drilltusk" : (141, (0,0,0), (0,3,10)),
                "Dreadqueen" : (142, (0,0,0), (0,3,10)),
                "Crystalbeard" : (143, (0,0,0), (0,3,10)),
                "Silverwind" : (144, (0,0,0), (0,3,10)),
                "Deadeye" : (145, (0,0,0), (0,3,10)),
                "Dreadking" : (146, (0,0,0), (0,3,10)),
                "Thunderlord" : (147, (0,0,0), (0,3,10)),
                "Grimclaw" : (148, (0,0,0), (0,3,10)),
                "Hellblade" : (149, (0,0,0), (0,3,10)),
                "Nightcloak" : (150, (0,0,0), (0,3,10)),
                "Rustrazor" : (151, (0,0,0), (0,3,10)),
                "Soulseer" : (152, (0,0,0), (0,3,10)),
                "Boltreaver" : (153, (0,0,0), (0,3,10)),
                "Elderfrost" : (154, (0,0,0), (0,3,10)),
                "Bloodbath" : (155, (0,0,0), (0,3,10)),
                "Redhelm X" : (156, (0,0,0), (0,3,10)),
                "Snowbaron X" : (157, (0,0,0), (0,3,10)),
                "Stonefist X" : (158, (0,0,0), (0,3,10)),
                "Drilltusk X" : (159, (0,0,0), (0,3,10)),
                "Dreadqueen X" : (160, (0,0,0), (0,3,10)),
                "Crystalbeard X" : (161, (0,0,0), (0,3,10)),
                "Silverwind X" : (162, (0,0,0), (0,3,10)),
                "Deadeye X" : (163, (0,0,0), (0,3,10)),
                "Dreadking X" : (164, (0,0,0), (0,3,10)),
                "Thunderlord X" : (165, (0,0,0), (0,3,10)),
                "Grimclaw X" : (166, (0,0,0), (0,3,10)),
                "Hellblade X" : (167, (0,0,0), (0,3,10)),
                "Nightcloak X" : (168, (0,0,0), (0,3,10)),
                "Rustrazor X" : (169, (0,0,0), (0,3,10)),
                "Soulseer X" : (170, (0,0,0), (0,3,10)),
                "Boltreaver X" : (171, (0,0,0), (0,3,10)),
                "Elderfrost X" : (172, (0,0,0), (0,3,10)),
                "Bloodbath X" : (173, (0,0,0), (0,3,10)),
                "-" : (174, (0,0,0), (-1,-1,-1))
            }
        self.readIn()

    def readIn(self):
        '''
        This function loads charms from the save file. CSV file must be in the following format:
        rarity,skill1 name,skill1 points,skill2 name,skill2 points,slots\n
        no spaces.
        Takes O(n^2) for completion.
        '''
        try:
            dataFile = open("charmData.csv","r")
            for line in dataFile:
                params = line.split(",")
                if params[4] == "-":
                    params[4] = 0
                if params[5] == "-":
                    params[5] = 0
                self.addCharm(Charm(int(params[0]), params[1], int(params[2]), params[3], int(params[4]), int(params[5])))
        except:
            dataFile = open("charmData.csv","w")

    def writeOut(self):
        '''
        This function writes all currently stored charms to the save file in an appropriate CSV format that readIn() can read.
        '''
        dataFile = open("charmData.csv","w")
        for i in range(len(self.charmList)):
            dataFile.write(self.charmList[i].csvReadyString()+"\n")

    def insertMain(self, charm):
        '''
        This function inserts a charm into the correct position of the charm list.
        The implementation takes O(n) operations to complete.

        Parameters
        ----------
        charm : Charm
            This is the charm that will be inserted into the charm list.
        '''
        destIndex = 0
        if len(self.charmList) == 0:
            self.charmList.append(charm)
            return

        #The growing list of conditions in each while loop is to ensure that the charms don't move out of their previous bound.
        #move to correct rarity
        while destIndex<len(self.charmList) and self.charmList[destIndex].rarity>charm.rarity:
            destIndex+=1
        if destIndex==len(self.charmList):
            self.charmList.append(charm)
            return
        if self.charmList[destIndex].rarity<charm.rarity:
            self.charmList.insert(destIndex, charm)
            return
        #move to correct primary skill
        while destIndex<len(self.charmList) and self.skillDict[self.charmList[destIndex].skill1[0]]<self.skillDict[charm.skill1[0]] and charm.rarity == self.charmList[destIndex].rarity:
            destIndex+=1
        if destIndex==len(self.charmList):
            self.charmList.append(charm)
            return
        if self.skillDict[self.charmList[destIndex].skill1[0]] > self.skillDict[charm.skill1[0]] or self.charmList[destIndex].rarity<charm.rarity:
            self.charmList.insert(destIndex, charm)
            return
        #move to correct position within primary skill based on skill points
        while destIndex<len(self.charmList) and self.charmList[destIndex].skill1[1]>charm.skill1[1] and charm.rarity == self.charmList[destIndex].rarity and charm.skill1[0] == self.charmList[destIndex].skill1[0]:
            destIndex+=1
        if destIndex==len(self.charmList):
            self.charmList.append(charm)
            return
        if self.charmList[destIndex].skill1[1]<charm.skill1[1] or self.skillDict[self.charmList[destIndex].skill1[0]] > self.skillDict[charm.skill1[0]]:
            self.charmList.insert(destIndex, charm)
            return
        #move to correct position within primary skill based on secondary skill
        while destIndex<len(self.charmList) and self.skillDict[self.charmList[destIndex].skill2[0]]<self.skillDict[charm.skill2[0]] and charm.rarity == self.charmList[destIndex].rarity and charm.skill1[0] == self.charmList[destIndex].skill1[0] and self.charmList[destIndex].skill1[1] == charm.skill1[1]:
            destIndex+=1
        if destIndex==len(self.charmList):
            self.charmList.append(charm)
            return
        if self.skillDict[self.charmList[destIndex].skill2[0]]>self.skillDict[charm.skill2[0]] or self.charmList[destIndex].skill1[1]<charm.skill1[1]:
            self.charmList.insert(destIndex, charm)
            return
        #move to correct position within primary skill based on skill points
        while destIndex<len(self.charmList) and self.charmList[destIndex].skill2[1]>charm.skill2[1] and charm.rarity == self.charmList[destIndex].rarity and charm.skill1[0] == self.charmList[destIndex].skill1[0] and self.charmList[destIndex].skill1[1] == charm.skill1[1] and charm.skill2[0] == self.charmList[destIndex].skill2[0]:
            destIndex+=1
        if destIndex==len(self.charmList):
            self.charmList.append(charm)
            return
        if self.charmList[destIndex].skill2[1]<charm.skill2[1] or self.skillDict[self.charmList[destIndex].skill2[0]]>self.skillDict[charm.skill2[0]]:
            self.charmList.insert(destIndex, charm)
            return
        #Move to the final position based on decoration slots
        while destIndex<len(self.charmList) and self.charmList[destIndex].slots>charm.slots and charm.rarity == self.charmList[destIndex].rarity and charm.skill1[0] == self.charmList[destIndex].skill1[0] and self.charmList[destIndex].skill1[1] == charm.skill1[1] and charm.skill2[0] == self.charmList[destIndex].skill2[0] and self.charmList[destIndex].skill2[1] == charm.skill2[1]:
            destIndex+=1
        if destIndex==len(self.charmList):
            self.charmList.append(charm)
            return
        elif self.charmList[destIndex].slots < charm.slots or self.charmList[destIndex].skill2[1]<charm.skill2[1]:
            self.charmList.insert(destIndex, charm)
            return
        if destIndex==len(self.charmList):
            self.charmList.append(charm)
        else:
            self.charmList.insert(destIndex, charm)


    def isBest(self, charm):
        '''
        This function checks to see if there are any charms with a higher point yield for either points in the charm passed in.
        If there are, then it returns False. If the charm passed in is better than all others for one of or both skills, then it returns True.

        Parameters
        ----------
        charm: Charm
            The charm that you would like to check

        Returns
        -------
        boolean
            Whether or not the passed charm is the best for one or both skills
        '''
        skill1Total = self.skillTotal(charm.skill1, charm.slots)
        skill2Total = self.skillTotal(charm.skill2, charm.slots)
        #If there are no entries for the given skill, it's automatically the current best.
        if charm.skill1[0] not in self.bestDict:
                self.insertBest(charm, charm.skill1[0])
        #Otherwise, check to see if the first or 2nd skill of the current best charm is better than the passed charm's first skill.
        else:
            skill1Best = self.bestDict[charm.skill1[0]]
            if skill1Best.skill1[0] == charm.skill1[0]:
                skill1BestTotal = self.skillTotal(skill1Best.skill1, skill1Best.slots)
            else:
                skill1BestTotal = self.skillTotal(skill1Best.skill2, skill1Best.slots)
            if (skill1Total > skill1BestTotal) or (skill1Total == skill1BestTotal and charm.slots > skill1Best.slots):
                self.insertBest(charm, charm.skill1[0])
        #Repeat check for skill2.
        if charm.skill2[0] not in self.bestDict:
                self.insertBest(charm, charm.skill2[0])
        else:
            skill2Best = self.bestDict[charm.skill2[0]]
            if skill2Best.skill1[0] == charm.skill2[0]:
                skill2BestTotal = self.skillTotal(skill2Best.skill1, skill2Best.slots)
            else:
                skill2BestTotal = self.skillTotal(skill2Best.skill2, skill2Best.slots)
            if (skill2Total > skill2BestTotal) or (skill2Total == skill2BestTotal and charm.slots > skill2Best.slots):
                self.insertBest(charm, charm.skill2[0])

    def hasMaxedPoints(self, charm):
        '''
        This function checks to see if the given charm has the maximum possible number of points for either its first or second skill.

        Parameters
        ----------
        charm: Charm
            The charm that will be checked

        Returns
        -------
        boolean
            Whether or not the given charm has the max number of points for either skill
        '''
        #Are the points for skill 1 the same as the maximum number possible as recorded in the skill dictionary?
        if charm.skill1[1] == self.skillDict[charm.skill1[0]][2][0]:
            return True
        elif charm.skill2[1] == self.skillDict[charm.skill2[0]][2][1]:
            return True
        return False

    def skillTotal(self, skillTuple, slots):
        '''
        This function gives the maximum possible number of points possible for a skill given the skill tuple, and the number of slots the charm has.

        Parameters
        ----------
        skillTuple: tuple
            Tuple of a skill name and points towards that skill.

        slots: int
            The number of decoration slots a charm has

        Returns
        -------
        int
            The total number of points towards the given skill possible, given a number of slots.
        '''
        skillTotal = skillTuple[1]
        if slots>0:
            skillTotal+=self.skillDict[skillTuple[0]][1][slots-1]
        return skillTotal

    def inBest(self, charm):
        '''
        Checks to see if the given charm has the most points for either of its two skills.

        Parameters
        ----------
        charm: Charm
            The charm to be searched for.

        Returns
        -------
        boolean
            Whether or not the charm was the best for either skill.
        '''
        if self.bestDict[charm.skill1[0]] == charm or self.bestDict[charm.skill2[0]] == charm:
            return True
        return False

    def insertBest(self, charm, skill):
        '''
        This function marks the given charm as the best charm for the given skill.

        Parameters
        ----------
        charm: Charm
            The charm that will be marked.

        skill: str
            The name of the skill the charm will be marked for.
        '''
        self.bestDict[skill] = charm

    def addCharm(self, charm):
        '''
        This function adds a charm to the CharmManager. Both inserts into the main collection, and also updates the best charms if necessary.
        Parameters
        ----------
        charm: Charm
            A new charm to add to the CharmManager
        '''
        self.insertMain(charm)
        if self.isBest(charm):
            self.insertBest(charm)

    def recycle3(self):
        '''
        This function selects three unimportant charms from the bottom of the sorted list, removes them, and returns them.

        Returns
        -------
        list
            A list of the three charms removed
        '''
        toRemove = [0]*3
        place = 2
        i=len(self.charmList)-1
        while place >=0 and i >= 0 and self.charmList[i].rarity<8:
            if not self.inBest(self.charmList[i]) and not self.hasMaxedPoints(self.charmList[i]):
                toRemove[place] = self.charmList.pop(i)
                place-=1
            i-=1
        return toRemove

    def removeCharm(self, charm):
        '''
        This function removes the specified charm. It offers a warning if the charm is the best charm owned for either skill, or if it has the max available points for either skill.

        Parameters
        ----------
        charm: Charm
            The charm to be removed
        '''
        if not self.inBest(charm) and not self.hasMaxedPoints(charm):
            self.charmList.remove(charm)
        else:
            if input("This charm is protected, as it gives the most points for one of its skills. Do you still want to remove it? Y/N\n") == "Y":
                self.charmList.remove(charm)
                #replace previous best
                for i in self.charmList:
                    if self.isBest(i):
                        self.insertBest(i)
                if self.bestDict[charm.skill1[0]]:
                    self.bestDict.pop(charm.skill1[0])
                if self.bestDict[charm.skill2[0]]:
                    self.bestDict.pop(charm.skill2[0])

    def displayAll(self):
        '''
        This function prints all charms stored by the CharmManager object.
        Marks charms that are either the best charm owned for the given skill, or has the maximum available points for either skill, by using an "*".
        '''
        for i in self.charmList:
            if self.hasMaxedPoints(i) or self.inBest(i):
                print("* "+str(i))
            else:
                print("  "+str(i))

    def displaySkill(self, skill):
        '''
        This function prints all charms that have a given skill, listing those with that skill as skill1 first, and then those with it as skill2 second.

        Parameters
        ----------
        skill: str
            The skill that the user would like to find the charms of.
        '''
        #Sacrificing a bit of efficiecy for a nicer output.
        for i in self.charmList:
            if i.skill1[0]==skill:
                if self.hasMaxedPoints(i) or self.inBest(i):
                    print("* "+str(i))
                else:
                    print("  "+str(i))
        for i in self.charmList:
            if i.skill2[0]==skill:
                if self.hasMaxedPoints(i) or self.inBest(i):
                    print("* "+str(i))
                else:
                    print("  "+str(i))

    def displayBest(self):
        '''
        Displays all of the charms marked as the best owned for either skill.
        '''
        for i in self.bestDict.keys():
            print(i+" : " + str(self.bestDict[i]))

    def displayBestSkill(self, skill):
        '''
        Displays all of the charms marked as the best owned for either skill, for a given skill.

        Parameters
        ----------
        skill: str
            The skill that the user would like to find the best charm of.
        '''
        print(self.bestDict[skill])

if __name__ == "__main__":
    charmSession = CharmManager()
    print("Welcome to Liam's MHGU Charm Manager!")
    mainMenu = "Enter the number cooresponding to your choice.\n 1: Display All Charms\n 2: Display Charms w/ a Certain Skill\n 3: Display All Best Charms\n 4: Display Best Charm for a Certain Skill\n 5: Add a New Charm\n 6: Recycle 3 Spares for melding\n 7: Trash a charm\n 8: Secret Dangerous Options\n 9: Quit\n"
    while True:
        try:
            selection = input(mainMenu)
            if selection  == "1":
                charmSession.displayAll()
            elif selection == "2":
                skill = input("Select which skill?\n")
                charmSession.displaySkill(skill)
            elif selection == "3":
                charmSession.displayBest()
            elif selection == "4":
                skill = input("Select which skill?\n")
                charmSession.displayBestSkill(skill)
            elif selection == "5":
                newCharm = input("Enter your new charm. Format: rarity,skill 1,skill1 points,skill2,skill2 points,slots\n")
                #Convert string into usable parameters for charm
                newCharm = newCharm.split(",")
                if newCharm[4] == "-":
                    newCharm[4] = 0
                if newCharm[5] == "-":
                    newCharm[5] = 0
                charmSession.addCharm(Charm(int(newCharm[0]), newCharm[1], int(newCharm[2]), newCharm[3], int(newCharm[4]), int(newCharm[5])))
            elif selection == "6":
                doomedCharms = charmSession.recycle3()
                print("Recycle the following charms:")
                for i in doomedCharms:
                    print(i)
            elif selection == "7":
                deadCharm = input("Enter the charm you wish to remove. Format: rarity,skill 1,skill1 points,skill2,skill2 points,slots\n")
                #Convert string into usable parameters for charm
                deadCharm = deadCharm.split(",")
                if deadCharm[4] == "-":
                    deadCharm[4] = 0
                if deadCharm[5] == "-":
                    deadCharm[5] = 0
                charmSession.removeCharm(Charm(int(deadCharm[0]), deadCharm[1], int(deadCharm[2]), deadCharm[3], int(deadCharm[4]), int(deadCharm[5])))
            elif selection =="8":
                secretOptions = "Enter the number cooresponding to your choice.\n 1: Clear All Charms\n 2: Load Backup File\n 3: Save to Backup\n 4: Return to Main Menu\n"
                secretSelection = input(secretOptions)
                if secretSelection == "1":
                    #Resets charm lists, and then overwrites the save file.
                    charmSession.charmList = []
                    charmSession.bestDict = {}
                    charmSession.writeOut()
                elif secretSelection == "2":
                    #Loads the backup save file, and then overwrites the main save file, finally restarting the current charm session.
                    backupFile = open("charmData_backup.csv","r")
                    dataFile = open("charmData.csv","w")
                    for i in backupFile:
                        dataFile.write(i)
                    backupFile.close()
                    dataFile.close()
                    charmSession = CharmManager()
                elif secretSelection == "3":
                    charmSession.writeOut()
                    backupFile = open("charmData_backup.csv","w")
                    dataFile = open("charmData.csv","r")
                    for i in dataFile:
                        backupFile.write(i)
                    backupFile.close()
                    dataFile.close()
                    charmSession = CharmManager()
                elif secretSelection == "4":
                    continue
                else:
                    print(secretSelection)
                    raise Error
            elif selection == "9":
                break
            else:
                raise Error
        except:
            print("You made an error in your input. Please try again.")
    charmSession.writeOut()
    print("Come again!")
