todoList = [""]

rodando = True


while rodando == True:

    #definição da tarefa
    task = input("digite uma tarefa: ")
    
    #atribuição da tarefa á lista de tarefas usando a punção ".append()"
    todoList.append(task)
    
    #show list
    print ("\nSuas tarefas são:\n",todoList,"\n\ndigite 'sair' para parar o programa\ndigite 'remover' para remover uma tarefa\n")
    
    # QUIT
    if task == "sair":
        rodando = False
        todoList.remove("sair")
    elif task == "remover":
        removeTask = input('qual tarefa voce deseja remover?\n')
        todoList.remove(removeTask)
        todoList.remove('remover')
        print('todoList')
        removeTask = ""

#basico...