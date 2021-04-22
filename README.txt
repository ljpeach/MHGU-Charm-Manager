ljpeach18-CharmManager.py
Running this file boots a charm management tool for Monster Hunter Generations Ultimate. The following prompt is all that's needed:

  python3 ljpeach18-CharmManager.py

The UI is as follows:

    Enter the number corresponding to your choice.
     1: Display All Charms
     2: Display Charms w/ a Certain Skill
     3: Display All Best Charms
     4: Display Best Charm for a Certain Skill
     5: Add a New Charm
     6: Recycle 3 Spares for melding
     7: Trash a charm
     8: Secret Dangerous Options
     9: Quit

1: Displays the charms stored within the tool. These will carry over from session to session, assuming the tool doesn't encounter any errors or keyboard interrupts.
    Uses an * to denote when a charm is either the best charm owned for either of its skills, or if either skill has the max number of points available.
    Ex: Tenderizer can give a maximum of 6 points in skill1's slot, and 5 in skill2.
2: Same as 1, but allows the user to specify a skill to limit the charm selection. Also uses an asterisk to denote protected charms.
3: Displays all the best in skill charms. Unfortunately, skills are not displayed in the proper order.
4: Same as 3, but allows the user to specify a skill to limit the charm selection.
5: Allows the user to add a new charm. The input must be in the following format:
    rarity,skill 1,skill1 points,skill2,skill2 points,slots
   No spaces.
   Rarity ranges from 10 - 1, but this tool will not penalize you for going out of range.
   Valid skills will be listed at the very bottom of this file. The quotation marks should not be included.
6: Chooses the bottom 3 unprotected charms in the list for recycling. Removes those three charms from the list.
7: Allows the user to remove a specified charm. Uses the same format as #5.
8: This menu option opens a submenu with more impactful commands that could prove dangerous if haphazardly selected.

    The UI is as follows:

      Enter the number corresponding to your choice.
       1: Clear All Charms
       2: Load Backup File
       3: Save to Backup
       4: Return to Main Menu

    1: Removes all charms from the management tool, and wipes the save file as well.
    2: Restores charms from a backup file, and rewrites the management tool. Fairly good for demos.
    3: Saves the current session to the save file and the backup file.
    4: Returns to the main menu, with no alterations.

  The Charm Manager sorts charms according to each attribute. Rarity takes priority, and next is skill1, skill1 points, so on and so forth
  down the list as seen in the format shown in 5:.
  Rarity is in descending order,
  skills are sorted in ascending order,
  skill points are in descending order,
  slots are in descending order.
  This is the same as it is in game.

  The Charm Manager comes with three additional files:

    charmData.csv
      This is the file that contains save data for the manager. This file should not be deleted, although the manager will create a new blank version if deleted.
      Deleting can result in a loss of saved data.
    charmData_backup.csv
      This file contains a backup for stored charms. The user can revert back to this file through the 8: Secret Dangerous Options menu.
    csvScramble.py
      This file allows the user to shuffle the save data file. This holds no real purpose outside of demonstrating the manager's sorting algorithm.


csvScramble.py
  This file can be used to shuffle the contents of the charm manager's main data file. It's has no real purpose other than demonstrating that the charm manager's sorting algorithm is
  successful in producing the correct result each time.

  This file can be run using:

    python3 csvScramble.py

  The charm manager's save file should be unscrambled after running once.

List of all valid charm skills (In sorting order):
-------------------------------
"Poison"
"Paralysis"
"Sleep"
"Stun"
"Hearing"
"Wind Res"
"Tremor Res"
"Bind Res"
"Heat Res"
"Cold Res"
"Coldblooded"
"Hotblooded"
"Anti Theft"
"Def Lock"
"Frenzy Res"
"Biology"
"Bleeding"
"Attack"
"Defense"
"Health"
"Fire Res"
"Water Res"
"Thunder Res"
"Ice Res"
"Dragon Res"
"Blight Res"
"Fire Atk"
"Water Atk"
"Thunder Atk"
"Ice Atk"
"Dragon Atk"
"Elemental"
"Status"
"Sharpener"
"Handicraft"
"Sharpness"
"Fencing"
"Grinder"
"Blunt"
"Crit Draw"
"Punish Draw"
"Sheathing"
"Sheathe Sharpen"
"Bladescale"
"Reload Spd"
"Recoil"
"Precision"
"Normal Up"
"Pierce Up"
"Pellet Up"
"Heavy Up"
"Normal S"
"Pierce S"
"Pellet S"
"Crag S"
"Clust S"
"Poison C"
"Para C"
"Sleep C"
"Power C"
"Elem C"
"Close Range C"
"Exhaust C"
"Blast C"
"Rapid Fire"
"Dead Eye"
"Loading"
"Haphazard"
"Ammo Saver"
"Expert"
"Tenderizer"
"Chain Crit"
"Crit Status"
"Crit Element"
"Critical Up"
"Negative Crit"
"Fast Charge"
"Stamina"
"Constitution"
"Stam Recov"
"Distance Runner"
"Evasion"
"Evade Dist"
"Bubble"
"Guard"
"Guard Up"
"KO"
"Stam Drain"
"Maestro"
"Artillery"
"Destroyer"
"Bomb Boost"
"Gloves Off"
"Spirit"
"Unscathed"
"Chance"
"Dragon Spirit"
"Potential"
"Survivor"
"Furor"
"Crisis"
"Guts"
"Sense"
"Team Player"
"Team Leader"
"Mounting"
"Vault"
"Insight"
"Endurance"
"Prolong SP"
"Psychic"
"Perception"
"Ranger"
"Transporter"
"Protection"
"Hero Shield"
"Rec Level"
"Rec Speed"
"Lasting Power"
"Wide Range"
"Hunger"
"Gluttony"
"Eating"
"Light Eater"
"Carnivore"
"Mycology"
"Botany"
"Combo Rate"
"Combo Plus"
"Speed Setup"
"Gathering"
"Honey"
"Charmer"
"Whim"
"Fate"
"Carving"
"Capturer"
"Redhelm"
"Snowbaron"
"Stonefist"
"Drilltusk"
"Dreadqueen"
"Crystalbeard"
"Silverwind"
"Deadeye"
"Dreadking"
"Thunderlord"
"Grimclaw"
"Hellblade"
"Nightcloak"
"Rustrazor"
"Soulseer"
"Boltreaver"
"Elderfrost"
"Bloodbath"
"Redhelm X"
"Snowbaron X"
"Stonefist X"
"Drilltusk X"
"Dreadqueen X"
"Crystalbeard X"
"Silverwind X"
"Deadeye X"
"Dreadking X"
"Thunderlord X"
"Grimclaw X"
"Hellblade X"
"Nightcloak X"
"Rustrazor X"
"Soulseer X"
"Boltreaver X"
"Elderfrost X"
"Bloodbath X"
