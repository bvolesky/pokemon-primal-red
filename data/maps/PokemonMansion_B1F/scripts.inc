PokemonMansion_B1F_MapScripts::
	map_script MAP_SCRIPT_ON_LOAD, PokemonMansion_B1F_OnLoad
	.byte 0

PokemonMansion_B1F_OnLoad::
	call_if_set FLAG_POKEMON_MANSION_SWITCH_STATE, PokemonMansion_EventScript_PressSwitch_B1F
	end

PokemonMansion_B1F_EventScript_Statue::
	lockall
	setvar VAR_0x8004, 3
	call PokemonMansion_EventScript_SecretSwitch
	playse SE_UNLOCK
	special DrawWholeMapView
	waitse
	releaseall
	end

PokemonMansion_B1F_EventScript_DiarySep1st::
	msgbox PokemonMansion_B1F_Text_MewtwoIsFarTooPowerful, MSGBOX_SIGN
	end

PokemonMansion_B1F_EventScript_Lewis::
	trainerbattle_single TRAINER_BURGLAR_LEWIS, PokemonMansion_B1F_Text_LewisIntro, PokemonMansion_B1F_Text_LewisDefeat
	msgbox PokemonMansion_B1F_Text_LewisPostBattle, MSGBOX_AUTOCLOSE
	end

PokemonMansion_B1F_EventScript_Ivan::
	trainerbattle_single TRAINER_SCIENTIST_IVAN, PokemonMansion_B1F_Text_IvanIntro, PokemonMansion_B1F_Text_IvanDefeat
	msgbox PokemonMansion_B1F_Text_IvanPostBattle, MSGBOX_AUTOCLOSE
	end


EventScript_PokemonMansion_B1F_MapScripts::
	map_script MAP_SCRIPT_ON_RESUME, EventScript_PokemonMansion_B1F_OnResume
	map_script MAP_SCRIPT_ON_TRANSITION, EventScript_PokemonMansion_B1F_OnTransition
	.byte 0

EventScript_PokemonMansion_B1F_OnResume::
	call_if_set FLAG_SYS_SPECIAL_WILD_BATTLE, EventScript_PokemonMansion_B1F_EventScript_TryRemoveMew
	end

EventScript_PokemonMansion_B1F_EventScript_TryRemoveMew::
    specialvar VAR_RESULT, GetBattleOutcome
    goto_if_ne VAR_RESULT, B_OUTCOME_CAUGHT, EventScript_Return
    setflag FLAG_HIDE_MEW
    removeobject VAR_LAST_TALKED
    return


EventScript_PokemonMansion_B1F_OnTransition::
	call_if_unset FLAG_FOUGHT_MEW, EventScript_PokemonMansion_B1F_EventScript_ShowMew
	end

EventScript_PokemonMansion_B1F_EventScript_ShowMew::
	clearflag FLAG_HIDE_MEW
	return

EventScript_PokemonMansion_B1F_EventScript_Mew::
    goto_if_questlog EventScript_ReleaseEnd
    special QuestLog_CutRecording
    lock
    faceplayer
    waitse
    playmoncry SPECIES_MEW, CRY_MODE_ENCOUNTER
    message CeruleanCave_B1F_Text_Mew
    waitmessage
    waitmoncry
    delay 20
    playbgm MUS_ENCOUNTER_GYM_LEADER, 0
    waitbuttonpress
    setwildbattle SPECIES_MEW, 50
    setflag FLAG_SYS_SPECIAL_WILD_BATTLE
    special StartLegendaryBattle
    waitstate
    clearflag FLAG_SYS_SPECIAL_WILD_BATTLE
    specialvar VAR_RESULT, GetBattleOutcome
    goto_if_eq VAR_RESULT, B_OUTCOME_WON, EventScript_PokemonMansion_B1F_EventScript_DefeatedMew
    goto_if_eq VAR_RESULT, B_OUTCOME_RAN, EventScript_PokemonMansion_B1F_EventScript_RanFromMew
    goto_if_eq VAR_RESULT, B_OUTCOME_PLAYER_TELEPORTED, EventScript_PokemonMansion_B1F_EventScript_RanFromMew

    setflag FLAG_FOUGHT_MEW
    setflag FLAG_HIDE_MEW
    removeobject VAR_LAST_TALKED
    release
    end



EventScript_PokemonMansion_B1F_EventScript_DefeatedMew::
	setflag FLAG_FOUGHT_MEW
	goto EventScript_RemoveStaticMon
	end

EventScript_PokemonMansion_B1F_EventScript_RanFromMew::
	setvar VAR_0x8004, SPECIES_MEW
	goto EventScript_MonFlewAway
	end




.set PokemonMansion_B1F_EventScript_Mew, EventScript_PokemonMansion_B1F_EventScript_Mew
.set PokemonMansion_B1F_EventScript_DefeatedMew, EventScript_PokemonMansion_B1F_EventScript_DefeatedMew
.set PokemonMansion_B1F_EventScript_RanFromMew, EventScript_PokemonMansion_B1F_EventScript_RanFromMew
.set PokemonMansion_B1F_EventScript_TryRemoveMew, EventScript_PokemonMansion_B1F_EventScript_TryRemoveMew
.set PokemonMansion_B1F_EventScript_ShowMew, EventScript_PokemonMansion_B1F_EventScript_ShowMew
