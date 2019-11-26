from functions import write_doc, get_text
import PySimpleGUI as gui


# Updates to add: GUI and API to define the words

print(gui.version)
if __name__ == "__main__":
    text = gui.PopupGetFile(title='Find document',
                            message='Choose document path')
    if text != "":
        file_name = gui.PopupGetText('Enter the name of the file for bold terms to be copied to')
        ok_message = gui.Popup(custom_text='Ok',
                               button_type=gui.Ok())

    else:
        error_message = gui.Popup(title="Error",
                                  custom_text='No Path Chosen',
                                  button_type=gui.Ok())

    text_list = get_text(text)
    write_doc(text_list, file_name)
