import streamlit
streamlit.title("Registration Plate Recognizer")

number_plate = streamlit.text_input("Enter Registration Number")
number_plate = number_plate.upper()


def identifier(number_plate):
  if number_plate[:2]=="SP":
    return (f"This Reg Plate belongs to Sabragamuva Province")
  elif number_plate[:2]=="CP":
    return ("This Reg Plate belongs to Central Province")
  elif number_plate[:2]=="EP":
    return ("This Reg Plate belongs to Eastern Province")
  elif number_plate[:2]=="NP":
    return ("This Reg Plate belongs to Nothern Province")
  elif number_plate[:2]=="WP":
    return ("This Reg Plate belongs to Western Province")
  elif number_plate[:2]=="NW":
    return ("This Reg Plate belongs to North Western Province")
  elif number_plate[:2]=="NC":
    return ("This Reg Plate belongs to North Central Province")
  elif number_plate[:2]=="UP":
    return ("This Reg Plate belongs to Uva Province")
  elif number_plate[:2]=="SB":
    return ("This Reg Plate belongs to Sabaragamuwa Province")
  else:
    return "Wrong Registration Number"

if streamlit.button("Find"):
    streamlit.write(identifier(number_plate))
else:
    pass
