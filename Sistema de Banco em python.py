#-*- coding: latin1 -*-

c1=0
nc1=0
sc1=0
c2=0
nc2=0
sc2=0
c3=0
nc3=0
sc3=0
c4=0
nc4=0
sc4=0
c5=0
nc5=0
sc5=0
c6=0
nc6=0
sc6=0
c7=0
nc7=0
sc7=0
c8=0
nc8=0
sc8=0
c9=0
nc9=0
sc9=0
c10=0
nc10=0
sc10=0
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
def menu():
    print "-----------------------"
    print ".:Sistema Bancário:."
    print "-----------------------"
    print "1. Cadastrar conta"
    print "-----------------------"
    print "2. Registrar depósito"
    print "3. Registrar saque"
    print "-----------------------"
    print "4. Listar clientes"
    print "5. Listar contas"
    print "-----------------------"
    print "6. Excluir conta"
    print "-----------------------"
    print "0. Sair"

def existe():
    print ""
    print "Essa conta já existe"

def exclusao():
    print "Conta excluida com sucesso."
    print ""
    
def nome(x):
    print ""
    print "Nome do proprietário é:",x
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
opcao="1"
while opcao != "0" and opcao != "não" and opcao != "nao" and opcao != "Não" and opcao != "Nao":
    menu()
    print""
    opcao = raw_input("Digite a opção: ")

    if opcao == "1":
        print ""
        print "-----------------"
        if c1 == 0:
            c1 = input("numero da conta: ")
            if c1 == c2 or c1 == c3 or c1 == c4 or c1 == c5 or c1 == c6 or c1 == c7 or c1 == c8 or c1 == c9 or c1 == c10:
                existe()
                c1 = 0
                nc1 = 0
                sc1 = 0
            elif c1 <= 0.0:
                c1 = 0
                print ""
                print "Número de conta invalido."
            else:
                nc1 = raw_input("nome do proprietário: ")
                print ""
                print "Conta criada com sucesso."
        elif c2 == 0:
            c2 = input("numero da conta: ")
            if c2 == c1 or c2 == c3 or c2 == c4 or c2 == c5 or c2 == c6 or c2 == c7 or c2 == c8 or c2 == c9 or c2 == c10:
                existe()
                c2 = 0
                nc2 = 0
                sc2 = 0
            elif c2 <= 0.0:
                c2 = 0
                print ""
                print "Número de conta invalido."
            else:
                nc2 = raw_input("nome do proprietário: ")
                print ""
                print "Conta criada com sucesso."
        elif c3 == 0:
            c3 = input("Número da conta: ")
            if c3 == c1 or c3 == c2 or c3 == c4 or c3 == c5 or c3 == c6 or c3 == c7 or c3 == c8 or c3 == c9 or c3 == c10:
                existe()
                c3 = 0
                nc3 = 0
                sc3 = 0
            elif c3 <= 0.0:
                c3 = 0
                print ""
                print "Número de conta invalido."
                c3 = 0
            else:
                nc3 = raw_input("nome do proprietário: ")
                print ""
                print "Conta criada com sucesso."
        elif c4 == 0:
            c4 = input("Número da conta: ")
            if c4 == c1 or c4 == c2 or c4 == c3 or c4 == c5 or c4 == c6 or c4 == c7 or c4 == c8 or c4 == c9 or c4 == c10:
                existe()
                c4 = 0
                nc4 = 0
                sc4 = 0
            elif c4 <= 0.0:
                c4 = 0
                print ""
                print "Número de conta invalido."
            else:
                nc4 = raw_input("nome do proprietário: ")
                print ""
                print "Conta criada com sucesso."
        elif c5 == 0:
            c5 = input("Número da conta: ")
            if c5 == c1 or c5 == c2 or c5 == c3 or c5 == c4 or c5 == c6 or c5 == c7 or c5 == c8 or c5 == c9 or c5 == c10:
                existe()
                c5 = 0
                nc5 = 0
                sc5 = 0
            elif c5 <= 0.0:
                c5 = 0
                print ""
                print "Número de conta invalido."
            else:
                nc5 = raw_input("nome do proprietário: ")
                print ""
                print "Conta criada com sucesso."
        elif c6 == 0:
            c6 = input("Número da conta: ")
            if c6 == c1 or c6 == c2 or c6 == c3 or c6 == c4 or c6 == c5 or c6 == c7 or c6 == c8 or c6 == c9 or c6 == c10:
                existe()
                c6 = 0
                nc6 = 0
                sc6 = 0
            elif c6 <= 0.0:
                c6 = 0
                print ""
                print "Número de conta invalido."
            else:
                nc6 = raw_input("nome do proprietário: ")
                print ""
                print "Conta criada com sucesso."
        elif c7 == 0:
            c7 = input("Número da conta: ")
            if c7 == c1 or c7 == c2 or c7 == c3 or c7 == c4 or c7 == c5 or c7 == c6 or c7 == c8 or c7 == c9 or c7 == c10:
                existe()
                c7 = 0
                nc7 = 0
                sc7 = 0
            elif c7 <= 0.0:
                c7 = 0
                print ""
                print "Número de conta invalido."
            else:
                nc7 = raw_input("nome do proprietário: ")
                print ""
                print "Conta criada com sucesso."
        elif c8 == 0:
            c8 = input("Número da conta: ")
            if c8 == c1 or c8 == c2 or c8 == c3 or c8 == c4 or c8 == c5 or c8 == c6 or c8 == c7 or c8 == c9 or c8 == c10:
                existe()
                c8 = 0
                nc8 = 0
                sc8 = 0
            elif c8 <= 0.0:
                c8 = 0
                print ""
                print "Número de conta invalido."
            else:
                nc8 = raw_input("nome do proprietário: ")
                print ""
                print "Conta criada com sucesso."
        elif c9 == 0:
            c9 = input("Número da conta: ")
            if c9 == c1 or c9 == c2 or c9 == c3 or c9 == c4 or c9 == c5 or c9 == c6 or c9 == c7 or c9 == c8 or c9 == c10:
                existe()
                c9 = 0
                nc9 = 0
                sc9 = 0
            elif c9 <= 0.0:
                c9 = 0
                print ""
                print "Número de conta invalido."
            else:
                nc9 = raw_input("nome do proprietário: ")
                print ""
                print "Conta criada com sucesso."
        elif c10 == 0:
            c10 = input("Número da conta: ")
            if c10 == c1 or c10 == c2 or c10 == c3 or c10 == c4 or c10 == c5 or c10 == c6 or c10 == c7 or c10 == c8 or c10 == c9:
                existe()
                c10 = 0
                nc10 = 0
                sc10 = 0
            elif c10 <= 0.0:
                c10 = 0
                print ""
                print "Número de conta invalido."
            else:
                nc10 = raw_input("nome do proprietário: ")
                print ""
                print "Conta criada com sucesso."
        elif c1 != 0 and c2 != 0 and c3 != 0 and c4 != 0 and c5 != 0 and c6 != 0 and c7 != 0 and c8 != 0 and c9 != 0 and c10 != 0:
            print ""
            print "Limite de contas excedido."
        print ""
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------        
    elif opcao == "2":
        print ""
        print "-----------------"
        conta = input("Digite uma conta: ")
        if conta != c1 and conta != c2 and conta != c3 and conta != c4 and conta != c5 and conta != c6 and conta != c7 and conta != c8 and conta != c9 and conta != c10 or conta == 0:
            print ""
            print"Essa conta não existe, para deposito."
            print ""
        else:
            deposito= input ("Digite o valor a ser depositado: ")
            print ""
            while deposito <= 0:
                if deposito <= 0:
                    print "Transação não concluida, informe outro valor para deposito."
                    print ""
                    deposito= input ("Digite o valor a ser depositado: ")
                    print ""
            if conta == c1 :
                sc1 += deposito
                print "Deposito realizado com sucesso."
                print ""
            elif conta == c2 :
                sc2 += deposito
                print "Deposito realizado com sucesso."
                print ""
            elif conta == c3 :
                sc3 += deposito
                print "Deposito realizado com sucesso."
                print ""
            elif conta == c4 :
                sc4 += deposito
                print "Deposito realizado com sucesso."
                print ""
            elif conta == c5 :
                sc5 += deposito
                print "Deposito realizado com sucesso."
                print ""
            elif conta == c6 :
                sc6 += deposito
                print "Deposito realizado com sucesso."
                print ""
            elif conta == c7 :
                sc7 += deposito
                print "Deposito realizado com sucesso."
                print ""
            elif conta == c8 :
                sc8 += deposito
                print "Deposito realizado com sucesso."
                print ""
            elif conta == c9 :
                sc9 += deposito
                print "Deposito realizado com sucesso."
                print ""
            elif conta == c10 :
                sc10 += deposito
                print "Deposito realizado com sucesso."
                print ""
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------            
    elif opcao == "3":
        print ""
        print "-----------------"
        conta = input("Digite o número da conta: ")
        if conta != c1 and conta != c2 and conta != c3 and conta != c4 and conta != c5 and conta != c6 and conta != c7 and conta != c8 and conta != c9 and conta != c10 or conta == 0:
            print ""
            print"Essa conta não existe, para se realizar um saque."
            print ""
        else:
            saque = input("Informe o valor do saque: ")
            print ""
            while saque <= 0:
                if saque <= 0:
                    print "Transação não concluida, informe outro valor para saque."
                    print ""
                    saque = input("Informe o valor do saque: ")
                    print ""
            if saque > sc1 and saque > sc2 and saque > sc3 and saque > sc4 and saque > sc5 and saque > sc6 and saque > sc7 and saque > sc8 and saque > sc9 and saque > sc10:
                print "Saldo insuficiente para a execução."
                print ""
            else:
                if conta == c1:
                    sc1 -= saque
                    print "Saque realizado com sucesso."
                    print ""
                elif conta == c2:
                    sc2 -= saque
                    print "Saque realizado com sucesso."
                    print ""
                elif conta == c4 :
                    sc4 -= saque
                    print "Saque realizado com sucesso."
                    print ""
                elif conta == c5 :
                    sc5 -= saque
                    print "Saque realizado com sucesso."
                    print ""
                elif conta == c6 :
                    sc6 -= saque
                    print "Saque realizado com sucesso."
                    print ""
                elif conta == c7 :
                    sc7 -= saque
                    print "Saque realizado com sucesso."
                    print ""
                elif conta == c8 :
                    sc8 -= saque
                    print "Saque realizado com sucesso."
                    print ""
                elif conta == c9 :
                    sc9 -= saque
                    print "Saque realizado com sucesso."
                    print ""
                elif conta == c10 :
                    sc10 -= saque
                    print "Saque realizado com sucesso."
                    print ""
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------            
    elif opcao == "4":
        print ""
        print "-----------------"
        if c1 > 0 :
            nome(nc1)
#-----------------------------------------------------------------------------------------------------------------
        if c2 > 0:
            nome(nc2)
#-----------------------------------------------------------------------------------------------------------------
        if c3 > 0:
            nome(nc3)
#-----------------------------------------------------------------------------------------------------------------
        if c4 > 0:
            nome(nc4)
#-----------------------------------------------------------------------------------------------------------------
        if c5 > 0:
            nome(nc5)
#-----------------------------------------------------------------------------------------------------------------
        if c6 > 0:
            nome(nc6)
#-----------------------------------------------------------------------------------------------------------------
        if c7 > 0:
            nome(nc7)
#-----------------------------------------------------------------------------------------------------------------
        if c8 > 0:
            nome(nc8)
#-----------------------------------------------------------------------------------------------------------------
        if c9 > 0:
            nome(nc9)
#-----------------------------------------------------------------------------------------------------------------
        if c10 > 0:
            nome(nc10)
        print ""
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
    elif opcao == "5":
        print ""
        print "-----------------"
        if c1 > 0:
            print ""
            print "Número da conta:", c1
            print "Proprietário da conta:", nc1
            print "Saldo da conta: R$ %.2f" % (sc1)
        if c2 > 0:
            print ""
            print "Número da conta:",c2
            print "Proprietário da conta:",nc2
            print "Saldo da conta: R$ %.2f" % (sc2)
        if c3 > 0:
            print ""
            print "Número da conta:",c3
            print "Proprietário da conta:",nc3
            print "Saldo da conta: R$ %.2f" % (sc3)
        if c4 > 0:
            print ""
            print "Número da conta:",c4
            print "Proprietário da conta:",nc4
            print "Saldo da conta: R$ %.2f" % (sc4)
        if c5 > 0:
            print ""
            print "Número da conta:",c5
            print "Proprietário da conta:",nc5
            print "Saldo da conta: R$ %.2f" % (sc5)
        if c6 > 0:
            print ""
            print "Número da conta:",c6
            print "Proprietário da conta:",nc6
            print "Saldo da conta: R$ %.2f" % (sc6)
        if c7 > 0:
            print ""
            print "Número da conta:",c7
            print "Proprietário da conta:",nc7
            print "Saldo da conta: R$ %.2f" % (sc7)
        if c8 > 0:
            print ""
            print "Número da conta:",c8
            print "Proprietário da conta:",nc8
            print "Saldo da conta: R$ %.2f" % (sc8)
        if c9 > 0:
            print ""
            print "Número da conta:",c9
            print "Proprietário da conta:",nc9
            print "Saldo da conta: R$ %.2f" % (sc9)
        if c10 > 0:
            print ""
            print "Número da conta:",c10
            print "Proprietário da conta:",nc10
            print "Saldo da conta: R$ %.2f" % (sc10)
        print ""
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
    elif opcao == "6":
        print ""
        print "-----------------"
        conta = input("Escolha a conta a ser excluida: ")
        print ""
        while conta <= 0:
            if conta <= 0:
                print "Número de conta invalido, digite novamente."
                print ""
                conta = input("Escolha a conta a ser excluida: ")
                print ""
        if conta != c1 and conta != c2 and conta != c3 and conta != c4 and conta != c5 and conta != c6 and conta != c7 and conta != c8 and conta != c9 and conta != c10:
            print "Essa conta não existe portanto não pode ser excluida."
            print ""
        elif conta == c1:
            c1 = 0
            nc1 = 0
            sc1 = 0
            exclusao()
        elif conta == c2:
            c2 = 0
            nc2 = 0
            sc2 = 0
            exclusao()
        elif conta == c3:
            c3 = 0
            nc3 = 0
            sc3 = 0
            exclusao()
        elif conta == c4:
            c4 = 0
            nc4 = 0
            sc4 = 0
            exclusao()
        elif conta == c5:
            c5 = 0
            nc5 = 0
            sc5 = 0
            exclusao()
        elif conta == c6:
            c6 = 0
            nc6 = 0
            sc6 = 0
            exclusao()
        elif conta == c7:
            c7 = 0
            nc7 = 0
            sc7 = 0
            exclusao()
        elif conta == c8:
            c8 = 0
            nc8 = 0
            sc8 = 0
            exclusao()
        elif conta == c9:
            c9 = 0
            nc9 = 0
            sc9 = 0
            exclusao()
        elif conta == c10:
            c10 = 0
            nc10 = 0
            sc10 = 0
            exclusao()
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------            
    while opcao != "sim" and opcao != "nao" and opcao != "não" and opcao != "Não" and opcao != "Nao" and opcao != "0":    
        print "Deseja executar uma nova ação?"
        print "Sim ou Não?"
        opcao = raw_input("")
        print ""
