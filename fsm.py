from transitions.extensions import GraphMachine

from utils import send_text_message, getMultiCPU, getMultiMB, getMultiRam, getMultiSSD, getMultiAirCooler, getMultiAIO, getMultiVGA, getMultiCase, getMultiPSU


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_searchLobby(self, event):
        return True

    def on_enter_searchLobby(self, event):
        print('On search lobby')

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
        return text.lower() == 'search psu'

    def is_going_to_showCPU(self, event):
        text = event.message.text
        return text.lower() != 'no'

    def is_going_to_showMotherboard(self, event):
        text = event.message.text
        return text.lower() != 'no'

    def is_going_to_showRam(self, event):
        text = event.message.text
        return text.lower() != 'no'

    def is_going_to_showSSD(self, event):
        text = event.message.text
        return text.lower() != 'no'

    def is_going_to_showAirCooler(self, event):
        text = event.message.text
        return text.lower() != 'no'

    def is_going_to_showAIO(self, event):
        text = event.message.text
        return text.lower() != 'no'

    def is_going_to_showVGA(self, event):
        text = event.message.text
        return text.lower() != 'no'

    def is_going_to_showCase(self, event):
        text = event.message.text
        return text.lower() != 'no'

    def is_going_to_showPSU(self, event):
        text = event.message.text
        return text.lower() != 'no'

    def is_going_back_to_user(self, event):
        text = event.message.text
        return text.lower() == 'no'

    def on_enter_searchCPU(self, event):
        print('On search CPU')
        getMultiCPU()

    def on_enter_searchMotherboard(self, event):
        print('On search Motherboard')
        getMultiMB()
    
    def on_enter_searchRam(self, event):
        print('On search Ram')
        getMultiRam()

    def on_enter_searchSSD(self, event):
        print('On search SSD')
        getMultiSSD()

    def on_enter_searchAirCooler(self, event):
        print('On search Air Cooler')
        getMultiAirCooler()

    def on_enter_searchAIO(self, event):
        print('On search AIO')
        getMultiAIO()

    def on_enter_searchVGA(self, event):
        print('On search VGA')
        getMultiVGA()

    def on_enter_searchCase(self, event):
        print('On search Case')
        getMultiCase()

    def on_enter_searchPSU(self, event):
        print('On search PSU')
        getMultiPSU()

    def on_enter_showCPU(self, event):
        print('On showCPU' + event.message.text)

    def on_enter_showMotherboard(self, event):
        print('On showMB' + event.message.text)
    
    def on_enter_showRam(self, event):
        print('On showRam' + event.message.text)

    def on_enter_showSSD(self, event):
        print('On showSSD' + event.message.text)

    def on_enter_showAirCooler(self, event):
        print('On showAirCooler' + event.message.text)

    def on_enter_showAIO(self, event):
        print('On showAIO' + event.message.text)

    def on_enter_showVGA(self, event):
        print('On showVGA' + event.message.text)

    def on_enter_showCase(self, event):
        print('On showCase' + event.message.text)

    def on_enter_showPSU(self, event):
        print('On showPSU' + event.message.text)

    

