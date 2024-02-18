import os
import PyPDF2
import json
import traceback

def read_file(file):
    if file.name.endswith(".pdf"):
        try:
            pdf_reader=PyPDF2.PdfFileReader(file)
            text=""
            for page in pdf_reader.pages:
                text+=page.extract_text()
            return text
            
        except Exception as e:
            raise Exception("error reading the PDF file")
        
    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    
    else:
        raise Exception(
            "unsupported file format only pdf and text file suppoted"
            )

def get_table_data(quiz_str):
    try:
        # convert the quiz from a str to dict
        print("I am here 6")
        print(quiz_str)
        print(type(quiz_str))
        print("The issue is after this")
        print(len(quiz_str))
        try:
            quiz_dict=json.loads(quiz_str)
            print(quiz_dict)
            print("Checking here")
        except json.decoder.JSONDecodeError:
            print("Not a valid json")

       # quiz_dict=json.loads(quiz_str)
        print("I am here 7")
        print(quiz_dict)
        quiz_table_data=[]
        print("I am here 777")
        # iterate over the quiz dictionary and extract the required information
        for key,value in quiz_dict.items():
            print("I am inside the for loop")
            mcq=value["mcq"]
            options=" || ".join(
                [
                    f"{option}-> {option_value}" for option, option_value in value["options"].items()
                 
                 ]
            )
            
            correct=value["correct"]
            quiz_table_data.append({"MCQ": mcq,"Choices": options, "Correct": correct})
        
        return quiz_table_data
        
    except Exception as e:
        traceback.print_exception(type(e), e, e.__traceback__)
        return False