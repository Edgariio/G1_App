from kivy.app import App
import os, sys
from kivy.resources import resource_add_path, resource_find
from kivy.properties import BooleanProperty
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen, ScreenManager


class HomeScreen(Screen):
    pass


class Test1Intro(Screen):
    pass


class Test1Q1(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! When you see a yield sign, you must slow down, stop if necessary and yield the ' \
                       'right-of-way. '
        self.button_disabled = True


class Test1Q2(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! This is a slow moving vehicle sign. '
        self.button_disabled = True


class Test1Q3(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! Always obey a police officer. '
        self.button_disabled = True


class Test1Q4(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should pull to the right as far as possible and stop.'
        self.button_disabled = True


class Test1Q5(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! This sign indicates a sharp bend or turn in the road ahead.'
        self.button_disabled = True


class Test1Q6(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! This sign indicates that you may park in the area during the times shown.'
        self.button_disabled = True


class Test1Q7(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should focus on steering and take your foot of the gas pedal to slow down.'
        self.button_disabled = True


class Test1Q8(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! All of these answers are correct.'
        self.button_disabled = True


class Test1Q9(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! In this case, you can drive with up to three passengers 19 or under between ' \
                       'midnight and 5 a.m. '
        self.button_disabled = True


class Test1Q10(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! This is a right turn only sign.'
        self.button_disabled = True


class Test1Q11(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! This is a do not block the intersection sign.'
        self.button_disabled = True


class Test1Q12(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You must adjust your speed and position to avoid a collision with other vehicles.'
        self.button_disabled = True


class Test1Q13(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should keep right and drive counter-clockwise until you arrive at your exit.'
        self.button_disabled = True


class Test1Q14(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! This sign indicates that there is no U-turn permitted.'
        self.button_disabled = True


class Test1Q15(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! This sign warns of road work ahead.'
        self.button_disabled = True


class Test1Q16(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should maintain a distance of 1 metre.'
        self.button_disabled = True


class Test1Q17(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should report the accident immediately to the nearest police office.'
        self.button_disabled = True


class Test1Q18(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! The licence will be suspended for 30 days from the day they surrender it.'
        self.button_disabled = True


class Test1Q19(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! This sign indicates that there are no bicycles permitted on this road.'
        self.button_disabled = True


class Test1Q20(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! This sign is a regulatory sign and indicates that the activity shown is not ' \
                       'permitted. '
        self.button_disabled = True


class Test1Q21(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! This sign warns of a lifting bridge ahead. '
        self.button_disabled = True


class Test1Q22(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! They must notify the Ministry of Transportation within 6 days.'
        self.button_disabled = True


class Test1Q23(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! This sign indicates that you may not drive straight through the intersection.'
        self.button_disabled = True


class Test1Q24(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should follow the detour marker until you return to the regular route.'
        self.button_disabled = True


class Test1Q25(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You can only answer if you pull over and park.'
        self.button_disabled = True


class Test1Q26(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! This sign warns of a traffic signal ahead.'
        self.button_disabled = True


class Test1Q27(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You will receive all of the above penalties if convicted.'
        self.button_disabled = True


class Test1Q28(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! This sign shows the route to the airport.'
        self.button_disabled = True


class Test1Q29(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should treat it as a four-way stop sign.'
        self.button_disabled = True


class Test1Q30(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! This is a hospital sign.'
        self.button_disabled = True


class Test1Q31(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You may turn left, go straight or turn right if the way is clear.'
        self.button_disabled = True


class Test1Q32(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! This sign indicates that snowmobiles may use this road.'
        self.button_disabled = True


class Test1Q33(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! This sign tells drivers that no passing is allowed on this road.'
        self.button_disabled = True


class Test1Q34(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! This sign tells drivers that idling for more than 3 minutes is not permitted.'
        self.button_disabled = True


class Test1Q35(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You must use low-beam headlights within 150 metres of an oncoming vehicle.'
        self.button_disabled = True


class Test1Q36(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! This sign indicates that drivers on the side road ahead do not have a clear view ' \
                       'of traffic. '
        self.button_disabled = True


class Test1Q37(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You will have your licence suspended for a minimum of 5 years.'
        self.button_disabled = True


class Test1Q38(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You can receive all of the above punishments.'
        self.button_disabled = True


class Test1Q39(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should stop if possible, if not, you should continue with caution.'
        self.button_disabled = True


class Test1Q40(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! This sign indicates that the pavement narrows ahead.'
        self.button_disabled = True


class Test1Fin(Screen):
    pass


class Test2Intro(Screen):
    pass


class Test2Q1(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You may receive all of the above penalties.'
        self.button_disabled = True


class Test2Q2(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should maintain a distance of at least 2 seconds behind the vehicle you are ' \
                       'following. '
        self.button_disabled = True


class Test2Q3(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! This sign warns the driver that railway tracks cross the road ahead.'
        self.button_disabled = True


class Test2Q4(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! This sign indicates a hidden school bus stop ahead.'
        self.button_disabled = True


class Test2Q5(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! Drivers are responsible for passengers who are under 16 years old to buckle up.'
        self.button_disabled = True


class Test2Q6(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should steer in the direction you want to go.'
        self.button_disabled = True


class Test2Q7(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! This is a "do not enter" sign.'
        self.button_disabled = True


class Test2Q8(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should slow down and yield the right-of-way if necessary.'
        self.button_disabled = True


class Test2Q9(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! This is a "school zone" sign.'
        self.button_disabled = True


class Test2Q10(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! This sign indicates that traffic may only travel in one direction.'
        self.button_disabled = True


class Test2Q11(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! This sign indicates that there may be water flowing over the road ahead.'
        self.button_disabled = True


class Test2Q12(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should give the proper signal and look if the lane change can be made safely.'
        self.button_disabled = True


class Test2Q13(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! This sign indicates a temporary detour from normal traffic.'
        self.button_disabled = True


class Test2Q14(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! This sign shows the upcoming roundabout exits and where they will take you.'
        self.button_disabled = True


class Test2Q15(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! It will cost you 6 demerit points and a maximum fine of up to $2000.'
        self.button_disabled = True


class Test2Q16(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You will be subject to licence cancellation and removal from the Graduated ' \
                       'Licensing System. '
        self.button_disabled = True


class Test2Q17(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You may be required to take out any of the above documents by a police officer.'
        self.button_disabled = True


class Test2Q18(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! This sign indicates the maximum safe speed on a ramp.'
        self.button_disabled = True


class Test2Q19(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! This sign tells the driver that they may not stop their vehicle in this area, ' \
                       'even for a moment. '
        self.button_disabled = True


class Test2Q20(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! It is permitted if the street or highway has two of more lanes for traffic in the ' \
                       'direction you are travelling. '
        self.button_disabled = True


class Test2Q21(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! This sign tells the driver to keep right of the traffic island.'
        self.button_disabled = True


class Test2Q22(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should stop, signal and make the turn while not interfering with traffic or ' \
                       'pedestrians. '
        self.button_disabled = True


class Test2Q23(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You will receive 2 demerit points.'
        self.button_disabled = True


class Test2Q24(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! The correct position is to the right of and as close to the centre line as possible.'
        self.button_disabled = True


class Test2Q25(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! This sign indicates a parking space only for vehicle displaying a valid Accessible '\
                       'Parking Permit. '
        self.button_disabled = True


class Test2Q26(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! This sign indicates facilities accessible by wheelchair.'
        self.button_disabled = True


class Test2Q27(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should not try to pass between them.'
        self.button_disabled = True


class Test2Q28(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should move to the right and allow the vehicle to pass.'
        self.button_disabled = True


class Test2Q29(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! This sign indicates that there are no pedestrians allowed on this road.'
        self.button_disabled = True


class Test2Q30(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! This sign indicates a pedestrian crossover.'
        self.button_disabled = True


class Test2Q31(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! These lines are used on a one-way street or highway that has more than one lane of '\
                       'traffic going in the same direction. '
        self.button_disabled = True


class Test2Q32(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! This sign indicates that a divided highway begins. '
        self.button_disabled = True


class Test2Q33(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! This sign indicates that a divided highway ends. '
        self.button_disabled = True


class Test2Q34(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You are not allowed to use any of the items listed while driving. '
        self.button_disabled = True


class Test2Q35(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! A sign with a green circle is a permissive sign. '
        self.button_disabled = True


class Test2Q36(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should stop before entering the intersection and wait until the traffic ahead ' \
                       'moves on. '
        self.button_disabled = True


class Test2Q37(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! It is because you cannot stop within the distance that you can see.'
        self.button_disabled = True


class Test2Q38(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should use low-beam headlights in heavy fog.'
        self.button_disabled = True


class Test2Q39(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You may drive at this speed only if the traffic and highway conditions allow ' \
                       'you to do so safely. '
        self.button_disabled = True


class Test2Q40(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should leave 20 metres between you and the school bus.'
        self.button_disabled = True


class Test2Fin(Screen):
    pass


class Test3Intro(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class Test3Q1(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! This sign indicates a hazard and the downward lines show the side you may safely ' \
                       'pass on. '
        self.button_disabled = True


class Test3Q2(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! Pedestrians crossing with the light have the right-of-way over others in this case.'
        self.button_disabled = True


class Test3Q3(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! This sign indicates that two roads going in the same direction are about to join ' \
                       'into one. '
        self.button_disabled = True


class Test3Q4(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! This driver is indicating that they are turning right.'
        self.button_disabled = True


class Test3Q5(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! This driver is indicating that they are turning left.'
        self.button_disabled = True


class Test3Q6(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! This driver is indicating that they are slowing down or stopping.'
        self.button_disabled = True


class Test3Q7(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! This sign indicates you may not park in this area.'
        self.button_disabled = True


class Test3Q8(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! They will receive a fine of $1000 and 3 demerit points.'
        self.button_disabled = True


class Test3Q9(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should pass just as you would with another car.'
        self.button_disabled = True


class Test3Q10(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! This sign warns of a traffic control person ahead.'
        self.button_disabled = True


class Test3Q11(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! This sign warns of a survey crew working ahead.'
        self.button_disabled = True


class Test3Q12(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! This sign warns of a bicycle crossing ahead.'
        self.button_disabled = True


class Test3Q13(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should stop and rest.'
        self.button_disabled = True


class Test3Q14(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! The maximum speed limit allowed is 50 km/h.'
        self.button_disabled = True


class Test3Q15(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You must be accompanied by a fully licensed driver with at least 4 years experience.'
        self.button_disabled = True


class Test3Q16(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should do any of the above if someone is tailgating you.'
        self.button_disabled = True


class Test3Q17(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! This sign indicates that the road is branching off ahead.'
        self.button_disabled = True


class Test3Q18(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! Only emergency vehicles responding to a call may carry a red light visible from ' \
                       'the front. '
        self.button_disabled = True


class Test3Q19(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! As a G2 driver your blood alcohol level must not be over 0.00%.'
        self.button_disabled = True


class Test3Q20(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! All of the above will be impaired with the use of alcohol or drugs.'
        self.button_disabled = True


class Test3Q21(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! This sign indicates that there is a steep hill ahead.'
        self.button_disabled = True


class Test3Q22(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! This sign indicates that there is a winding road ahead.'
        self.button_disabled = True


class Test3Q23(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should slow down and proceed with caution.'
        self.button_disabled = True


class Test3Q24(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You can carry 1 passenger aged 19 or under in this case.'
        self.button_disabled = True


class Test3Q25(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! The driver may not carry passengers in the house or boat trailer while on a highway.'
        self.button_disabled = True


class Test3Q26(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! This sign indicates that the paved surface ends ahead.'
        self.button_disabled = True


class Test3Q27(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! This sign indicates that the speed limit changes ahead to 50 km/h.'
        self.button_disabled = True


class Test3Q28(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You must use low-beam headlights within 60 metres when following another vehicle.'
        self.button_disabled = True


class Test3Q29(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You must stop and then proceed only when the signal turns green and the way is clear.'
        self.button_disabled = True


class Test3Q30(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! This sign indicates a bus entrance on the right.'
        self.button_disabled = True


class Test3Q31(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! This sign indicates a community zone where driving fines are increased.'
        self.button_disabled = True


class Test3Q32(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! This sign indicates a narrow bridge ahead.'
        self.button_disabled = True


class Test3Q33(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! This sign indicates a slight bend or curve in the road ahead.'
        self.button_disabled = True


class Test3Q34(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! During school hours when the lights flash, follow the speed limit shown.'
        self.button_disabled = True


class Test3Q35(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should stop and yield the right-of-way to the pedestrian.'
        self.button_disabled = True


class Test3Q36(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should not park within 3 metres of a fire hydrant.'
        self.button_disabled = True


class Test3Q37(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! Passing within 30 metres of a pedestrian crossover is prohibited.'
        self.button_disabled = True


class Test3Q38(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! You should stop at least 5 metres from the nearest rail.'
        self.button_disabled = True


class Test3Q39(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! It is illegal to reverse on a divided road with a speed limit of more than 80 km/h.'
        self.button_disabled = True


class Test3Q40(Screen):
    my_text = StringProperty('')
    button_disabled = BooleanProperty(False)

    def on_correct_click(self):
        self.my_text = 'Correct!'
        self.button_disabled = True

    def on_incorrect_click(self):
        self.my_text = 'Incorrect! Failing to yield will cost you 3 demerit points.'
        self.button_disabled = True


class Test3Fin(Screen):
    pass


class G1App(App):
    pass


if __name__ == '__main__':
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
    G1App().run()
