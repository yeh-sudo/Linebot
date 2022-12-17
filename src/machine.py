from src.fsm import TocMachine

def create_machine():
    machine = TocMachine(
        states=["user", "help", "fsm", "searchLobby", "searchCPU", "searchMotherboard", "searchRam", "searchSSD", "searchAirCooler", "searchAIO", "searchVGA", "searchCase", "searchPSU",
        "showCPU", "showMotherboard", "showRam", "showSSD", "showAirCooler", "showAIO", "showVGA", "showCase", "showPSU"],
        transitions=[
            {
                "trigger": "advance",
                "source": "user",
                "dest": "searchLobby",
                "conditions": "is_going_to_searchLobby",
            },
            {
                "trigger": "advance",
                "source": "searchLobby",
                "dest": "help",
                "conditions": "is_going_to_help",
            },
            {
                "trigger": "advance",
                "source": "searchLobby",
                "dest": "fsm",
                "conditions": "is_going_to_fsm",
            },
            {
                "trigger": "advance",
                "source": "searchLobby",
                "dest": "searchCPU",
                "conditions": "is_going_to_searchCPU",
            },
            {
                "trigger": "advance",
                "source": "searchLobby",
                "dest": "searchMotherboard",
                "conditions": "is_going_to_searchMotherboard",
            },
            {
                "trigger": "advance",
                "source": "searchLobby",
                "dest": "searchRam",
                "conditions": "is_going_to_searchRam",
            },
            {
                "trigger": "advance",
                "source": "searchLobby",
                "dest": "searchSSD",
                "conditions": "is_going_to_searchSSD",
            },
            {
                "trigger": "advance",
                "source": "searchLobby",
                "dest": "searchAirCooler",
                "conditions": "is_going_to_searchAirCooler",
            },
            {
                "trigger": "advance",
                "source": "searchLobby",
                "dest": "searchAIO",
                "conditions": "is_going_to_searchAIO",
            },
            {
                "trigger": "advance",
                "source": "searchLobby",
                "dest": "searchVGA",
                "conditions": "is_going_to_searchVGA",
            },
            {
                "trigger": "advance",
                "source": "searchLobby",
                "dest": "searchCase",
                "conditions": "is_going_to_searchCase",
            },
            {
                "trigger": "advance",
                "source": "searchLobby",
                "dest": "searchPSU",
                "conditions": "is_going_to_searchPSU",
            },
            {
                "trigger": "advance",
                "source": "searchCPU",
                "dest": "showCPU",
                "conditions": "is_going_to_showCPU",
            },
            {
                "trigger": "advance",
                "source": "showCPU",
                "dest": "showCPU",
                "conditions": "is_going_to_showCPU",
            },
            {
                "trigger": "advance",
                "source": "searchMotherboard",
                "dest": "showMotherboard",
                "conditions": "is_going_to_showMotherboard",
            },
            {
                "trigger": "advance",
                "source": "showMotherboard",
                "dest": "showMotherboard",
                "conditions": "is_going_to_showMotherboard",
            },
            {
                "trigger": "advance",
                "source": "searchRam",
                "dest": "showRam",
                "conditions": "is_going_to_showRam",
            },
            {
                "trigger": "advance",
                "source": "showRam",
                "dest": "showRam",
                "conditions": "is_going_to_showRam",
            },
            {
                "trigger": "advance",
                "source": "searchSSD",
                "dest": "showSSD",
                "conditions": "is_going_to_showSSD",
            },
            {
                "trigger": "advance",
                "source": "showSSD",
                "dest": "showSSD",
                "conditions": "is_going_to_showSSD",
            },
            {
                "trigger": "advance",
                "source": "searchAirCooler",
                "dest": "showAirCooler",
                "conditions": "is_going_to_showAirCooler",
            },
            {
                "trigger": "advance",
                "source": "showAirCooler",
                "dest": "showAirCooler",
                "conditions": "is_going_to_showAirCooler",
            },
            {
                "trigger": "advance",
                "source": "searchAIO",
                "dest": "showAIO",
                "conditions": "is_going_to_showAIO",
            },
            {
                "trigger": "advance",
                "source": "showAIO",
                "dest": "showAIO",
                "conditions": "is_going_to_showAIO",
            },
            {
                "trigger": "advance",
                "source": "searchVGA",
                "dest": "showVGA",
                "conditions": "is_going_to_showVGA",
            },
            {
                "trigger": "advance",
                "source": "showVGA",
                "dest": "showVGA",
                "conditions": "is_going_to_showVGA",
            },
            {
                "trigger": "advance",
                "source": "searchCase",
                "dest": "showCase",
                "conditions": "is_going_to_showCase",
            },
            {
                "trigger": "advance",
                "source": "showCase",
                "dest": "showCase",
                "conditions": "is_going_to_showCase",
            },
            {
                "trigger": "advance",
                "source": "searchPSU",
                "dest": "showPSU",
                "conditions": "is_going_to_showPSU",
            },
            {
                "trigger": "advance",
                "source": "showPSU",
                "dest": "showPSU",
                "conditions": "is_going_to_showPSU",
            },
            {
                "trigger": "go_back", 
                "source": ["fsm", "help", "searchCPU", "searchMotherboard", "searchRam", "searchSSD", "searchAirCooler", "searchAIO", "searchVGA", "searchCase", "searchPSU"], 
                "dest": "searchLobby"
            },
            {
                "trigger": "advance", 
                "source": ["searchCPU", "searchMotherboard", "searchRam", "searchSSD", "searchAirCooler", "searchAIO", "searchVGA", "searchCase", "searchPSU",
                "showCPU", "showMotherboard", "showRam", "showSSD", "showAirCooler", "showAIO", "showVGA", "showCase", "showPSU"], 
                "dest": "searchLobby",
                "conditions": "is_going_back_to_user"
            },
        ],
        initial="user",
        auto_transitions=False,
        show_conditions=True,
    )

    return machine