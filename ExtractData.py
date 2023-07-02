import re
import glob
import os
import xlsxwriter

# Define the regular expression patterns to extract Text1 and Text2
text1_pattern = r"\\([^\\]+)\.wav"
text2_pattern = r"(?<=keycenter=)(\d+)(?=\s)"
text3_pattern = r"(?<=lokey=)(\d+)(?=\s)"
text4_pattern = r"(?<=hikey=)(\d+)(?=\s)"

# Define the list of MIDI note names
note_names = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

while True:
    # Prompt the user to enter the directory where the sfz files are located
    directory = input("Enter the directory where the sfz files are located: ")
    # Exit the loop if the user enters "quit"
    if directory.lower() == "quit":
        break

    # Define the filename for the xlsx file
    xlsx_filename = f"{directory}/output.xlsx"

    # Create an xlsx file and add a worksheet
    workbook = xlsxwriter.Workbook(xlsx_filename)
    worksheet = workbook.add_worksheet()

    # Write the headers for the worksheet
    headers = ["File", "MIDI Note", "Low Key","High Key","Patch"]
    for i, header in enumerate(headers):
        worksheet.write(0, i, header)

    # Iterate over each txt file in the directory
    row = 1
    for file_name in glob.glob(f"{directory}/*.sfz"):

        # Open the txt file and extract Text1 and Text2
        with open(file_name, "r") as txt_file:
            text = txt_file.read()
            text_1_list = re.findall(text1_pattern, text)
            text_2_list = re.findall(text2_pattern, text)
            text_3_list = re.findall(text3_pattern, text)
            text_4_list = re.findall(text4_pattern, text)
            file_base_name = os.path.basename(file_name)

            # Write the text to the worksheet for each occurrence
            for i in range(len(text_1_list)):
                text_1 = text_1_list[i].strip()

                if i < len(text_2_list):
                    text_2 = int(text_2_list[i])
                    note_index = text_2 % 12
                    octave = (text_2 // 12) - 2
                    midi_note = f"{note_names[note_index]}{octave}"
                else:
                    text_2 = ""
                    midi_note = ""
                if i < len(text_2_list):
                    text_3 = int(text_3_list[i])
                    note_index = text_3 % 12
                    octave = (text_3 // 12) - 2
                    lomidi_note = f"{note_names[note_index]}{octave}"
                else:
                    text_3 = ""
                    lomidi_note = ""
                if i < len(text_4_list):
                    text_4 = int(text_4_list[i])
                    note_index = text_4 % 12
                    octave = (text_4 // 12) - 2
                    himidi_note = f"{note_names[note_index]}{octave}"
                else:
                    text_4 = ""
                    himidi_note = ""

                # Write Text1 and Text2 to the worksheet
                worksheet.write(row, 0, text_1)
                worksheet.write(row, 1, midi_note)
                worksheet.write(row, 2, lomidi_note)
                worksheet.write(row, 3, himidi_note)
                worksheet.write(row, 4, file_base_name)

                row += 1

    # Close the workbook
    workbook.close()

    print(f"Output written to {xlsx_filename}\n")

print("Done!")
