from flask import Flask, render_template, request
from Utils.temp_picker import picker


def render_settings():
    if request.method == "POST":
        set1 = request.form["test"]
        picker(set1)

    return render_template("settings.html")

