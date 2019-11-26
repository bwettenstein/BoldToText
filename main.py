from functions import write_doc, get_text
import PySimpleGUI as gui


print(gui.version)
if __name__ == "__main__":
    doc_file = gui.PopupGetFile(title='Find document',
                            message='Choose document path')
    # If the user chose a document and didn't just hit 'ok' this will then ask the user to enter the title of the docx
    # file where the bold terms will be copied to.
    if doc_file != "":
        file_name = gui.PopupGetText('Enter the name of the file for bold terms to be copied to')
        ok_message = gui.Popup(custom_text='Ok',
                               button_type=gui.Ok())

    else:
        error_message = gui.Popup(title="Error",
                                  custom_text='No Path Chosen',
                                  button_type=gui.Ok())

    text_list = get_text(doc_file)
    write_doc(text_list, file_name)
