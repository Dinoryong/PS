def solution(table, languages, preference):
    answer = ''
    return answer


python = 0
jave = 0
javascript = 0
c = 0
cplus = 0
csharp = 0
sql = 0
kotlin = 0
php = 0
for j in table:
    if table[j] == "PYTHON":
        python += 1
    elif table[j] == "JAVA":
        java += 1
    elif table[j] == "JAVASCRIPT":
        javascript += 1
    elif table[j] == "C":
        c += 1
    elif table[j] == "C++":
        cplus += 1
    elif table[j] == "C#":
        csharp += 1
    elif table[j] == "SQL":
        sql += 1
    elif table[j] == "KOTLIN":
        kotlin += 1
    elif table[j] == "PHP":
        php += 1

for i in languages:
    if languages[i] == "PYTHON":
        python = python * preference[i]
    elif languages[i] == "JAVA":
        java = java * preferenc[i]
    elif table[j] == "JAVASCRIPT":
        javascript = javascript * preference[i]
    elif table[j] == "C":
        c = c * preference[i]
    elif table[j] == "C++":
        cplus = cplus * preference[i]
    elif table[j] == "C#":
        csharp = csharp * preference[i]
    elif table[j] == "SQL":
        sql = sql * preferenc[i]
    elif table[j] == "KOTLIN":
        kotlin = kotlin * preference[i]
    elif table[j] == "PHP":
        php = php * preference[i]


