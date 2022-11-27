from fsm import TocMachine

def create_machine():
    machine = TocMachine(
        states=["user", "searchCPU", "searchMotherboard", "searchRam", "searchSSD", "searchAirCooler", "searchAIO", "searchVGA", "searchCase", "searchPSU",
        "showCPU", "showMotherboard", "showRam", "showSSD", "showAirCooler", "showAIO", "showVGA", "showCase", "showPSU"],
        transitions=[
            {
                "trigger": "advance",
                "source": "user",
                "dest": "searchCPU",
                "conditions": "is_going_to_searchCPU",
            },
            {
                "trigger": "advance",
                "source": "user",
                "dest": "searchMotherboard",
                "conditions": "is_going_to_searchMotherboard",
            },
            {
                "trigger": "advance",
                "source": "user",
                "dest": "searchRam",
                "conditions": "is_going_to_searchRam",
            },
            {
                "trigger": "advance",
                "source": "user",
                "dest": "searchSSD",
                "conditions": "is_going_to_searchSSD",
            },
            {
                "trigger": "advance",
                "source": "user",
                "dest": "searchAirCooler",
                "conditions": "is_going_to_searchAirCooler",
            },
            {
                "trigger": "advance",
                "source": "user",
                "dest": "searchAIO",
                "conditions": "is_going_to_searchAIO",
            },
            {
                "trigger": "advance",
                "source": "user",
                "dest": "searchVGA",
                "conditions": "is_going_to_searchVGA",
            },
            {
                "trigger": "advance",
                "source": "user",
                "dest": "searchCase",
                "conditions": "is_going_to_searchCase",
            },
            {
                "trigger": "advance",
                "source": "user",
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
                "source": "searchMotherboard",
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
                "source": "searchSSD",
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
                "source": "searchAIO",
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
                "source": "searchCase",
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
                "trigger": "go_back", 
                "source": ["searchCPU", "searchMotherboard", "searchRam", "searchSSD", "searchAirCooler", "searchAIO", "searchVGA", "searchCase", "searchPSU"], 
                "dest": "user"
            },
        ],
        initial="user",
        auto_transitions=False,
        show_conditions=True,
    )

    return machine