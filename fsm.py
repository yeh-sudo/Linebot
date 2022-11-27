from transitions.extensions import GraphMachine

from utils import send_text_message


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_searchCPU(self, event):
        text = event.message.text
        return text.lower() == "search cpu"

    def is_going_to_searchMotherboard(self, event):
        text = event.message.text
        return text.lower() == 'search motherboard'

    def is_going_to_searchRam(self, event):
        text = event.message.text
        return text.lower() == 'search ram'

    def is_going_to_searchSSD(self, event):
        text = event.message.text
        return text.lower() == 'search ssd'

    def is_going_to_searchAirCooler(self, event):
        text = event.message.text
        return text.lower() == 'search air cooler'

    def is_going_to_searchAIO(self, event):
        text = event.message.text
        return text.lower() == 'search aio'

    def is_going_to_searchVGA(self, event):
        text = event.message.text
        return text.lower() == 'search vga'

    def is_going_to_searchCase(self, event):
        text = event.message.text
        return text.lower() == 'search case'

    def is_going_to_searchPSU(self, event):
        text = event.message.text
        return text.lower() == 'search PSU'

    def is_going_to_showCPU(self, event):
        text = event.message.text
        return text.lower() == 'show cpu'

    def is_going_to_showMotherboard(self, event):
        text = event.message.text
        return text.lower() == 'show motherboard'

    def is_going_to_showRam(self, event):
        text = event.message.text
        return text.lower() == 'show ram'

    def is_going_to_showSSD(self, event):
        text = event.message.text
        return text.lower() == 'show ssd'

    def is_going_to_showAirCooler(self, event):
        text = event.message.text
        return text.lower() == 'show air cooler'

    def is_going_to_showAIO(self, event):
        text = event.message.text
        return text.lower() == 'show AIO'

    def is_going_to_showVGA(self, event):
        text = event.message.text
        return text.lower() == 'show vga'

    def is_going_to_showCase(self, event):
        text = event.message.text
        return text.lower() == 'show case'

    def is_going_to_showPSU(self, event):
        text = event.message.text
        return text.lower() == 'show psu'

    def on_enter_searchCPU(self, event):
        print('On search CPU')
        self.go_back()

    def on_enter_searchMotherboard(self, event):
        print('On search Motherboard')
        self.go_back()
    
    def on_enter_searchRam(self, event):
        print('On search Ram')
        self.go_back()

    def on_enter_searchSSD(self, event):
        print('On search SSD')
        self.go_back()

    def on_enter_searchAirCooler(self, event):
        print('On search Air Cooler')
        self.go_back()

    def on_enter_searchAIO(self, event):
        print('On search AIO')
        self.go_back()

    def on_enter_searchVGA(self, event):
        print('On search VGA')
        self.go_back()

    def on_enter_searchCase(self, event):
        print('On search Case')
        self.go_back()

    def on_enter_searchPSU(self, event):
        print('On search PSU')
        self.go_back()

    def on_enter_showCPU(self, event):
        print('On show CPU')

    def on_enter_showMotherboard(self, event):
        print('On show Motherboard')
    
    def on_enter_showRam(self, event):
        print('On show Ram')

    def on_enter_showSSD(self, event):
        print('On show SSD')

    def on_enter_showAirCooler(self, event):
        print('On show Air Cooler')

    def on_enter_showAIO(self, event):
        print('On show AIO')

    def on_enter_showVGA(self, event):
        print('On show VGA')

    def on_enter_showCase(self, event):
        print('On show Case')

    def on_enter_showPSU(self, event):
        print('On show PSU')

    

