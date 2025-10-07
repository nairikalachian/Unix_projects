# Task 1

text = "Before departure, all students leaving for exchange studies should fill in a specialized application form. An application should be submitted in 1 copy and not later than 2 weeks prior to departure for the exchange semester, provided that the students do not have any academic failure. The paper should be submitted to the International Academic Mobility Office (Volkhovsky per., 3, office 207, Tel.: +7 (812) 323 8447). A copy of the invitation letter from a host school - partner of GSOM SPbU has to be attached to the application."
st_str = "("
end_str = ", Tel."

st_ind = text.find(st_str) + 1 # Excluding the parenthesis
end_ind = text.find(end_str, st_ind) # Starting index count from the "("
address = text[st_ind:end_ind]

print(address)