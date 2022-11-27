from transitions.extensions import GraphMachine

from utils import send_text_message


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_searchCPU(self, event):
        text = event.message.text
        return text.lower() == 'search cpu'

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

    def on_enter_searchCPU():
        print('On search CPU')

    def on_enter_searchMotherboard():
        print('On search Motherboard')
    
    def on_enter_searchRam():
        print('On search Ram')

    def on_enter_searchSSD():
        print('On search SSD')

    def on_enter_searchAirCooler():
        print('On search Air Cooler')

    def on_enter_searchAIO():
        print('On search AIO')

    def on_enter_searchVGA():
        print('On search VGA')

    def on_enter_searchCase():
        print('On search Case')

    def on_enter_searchPSU():
        print('On search PSU')

    def on_enter_showCPU():
        print('On show CPU')

    def on_enter_showMotherboard():
        print('On show Motherboard')
    
    def on_enter_showRam():
        print('On show Ram')

    def on_enter_showSSD():
        print('On show SSD')

    def on_enter_showAirCooler():
        print('On show Air Cooler')

    def on_enter_showAIO():
        print('On show AIO')

    def on_enter_showVGA():
        print('On show VGA')

    def on_enter_showCase():
        print('On show Case')

    def on_enter_showPSU():
        print('On show PSU')

    

