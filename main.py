from tkinter import *

window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=50, height=50)
window.config(padx=20, pady=20)

# Label
is_equal_label = Label(text="is equal to", font=("Arial", 20))
is_equal_label.grid(column=0, row=1)

kilometer_label = Label(text="Km", font=("Arial", 20))
kilometer_label.grid(column=2, row=1)

miles_label = Label(text="Miles", font=("Arial", 20))
miles_label.grid(column=2, row=0)

kilometer_result_label = Label(text="", font=("Arial", 20))
kilometer_result_label.grid(column=1, row=1)


# Button
def miles_to_km():
    kilometer_result_label["text"] = f"{float(miles_input.get()) * 1.609}"


calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

# Entry
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

window.mainloop()
