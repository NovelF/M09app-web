#!/usr/bin/python3
import sys
import csv

with open('mail.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for i in reader:
        