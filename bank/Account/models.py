from django.db import models
import random
import string
from person.models import Person
from django.db.models import Max
from django.db import transaction
from django.db.models import Sum
import logging

logger = logging.getLogger('django')

class Account(models.Model):
    accID = models.CharField(max_length=20)
    cash = models.IntegerField()
    owner = models.ForeignKey("person.Person", on_delete=models.CASCADE, null=True)
    
    def q1(num):
        people = list(Person.objects.all())
        account_objects = []
        availableAccID = random.sample(range(100000,999999), num)
        for i in range(num):
            account_objects.append(Account(
                accID = str(availableAccID.pop()),
                cash = random.randint(0, 1000000),
                owner = random.choice(people)
            ))
        Account.objects.bulk_create(account_objects)

    def q2():
        accounts = Account.objects.all()
        return [(account.owner.name,account.cash)for account in accounts]
    
    def q3():
        max_cash = Account.objects.all().aggregate(Max('cash'))['cash__max']
        userWithMaxCash = Account.objects.get(cash=max_cash)
        logger.info(userWithMaxCash)
        return userWithMaxCash
    
    def q4():
        fiveAccountsWithMin = Account.objects.order_by('cash')[0:5]
        logger.info(fiveAccountsWithMin)
        return fiveAccountsWithMin
    
    def q5(senderAccID, receiverAccId, amount):
        with transaction.atomic():
            senderAcc = Account.objects.get(id=senderAccID)
            receiverAcc = Account.objects.get(id=receiverAccId)
            senderAcc.cash -= amount
            senderAcc.save()
            receiverAcc.cash += amount
            receiverAcc.save()

    def q6():
        satisfied = []
        accounts = Account.objects.all()
        for account in accounts:
            if int(account.accID) > account.cash:
                satisfied.append(account)
        logger.info(satisfied)
        return satisfied
    
    def q7():
        satisfied = []
        accounts = Account.objects.all()
        for account in accounts:
            if int(account.owner.nationalCode) > account.cash:
                satisfied.append(account)
        logger.info(satisfied)
        return satisfied
    
    def q9(name):
        accountsOfCurPerson = Account.objects.filter(owner_id__name = name)
        sumCash = accountsOfCurPerson.aggregate(Sum('cash'))
        logger.info(f'{name}:{sumCash}')
        return accountsOfCurPerson.aggregate(Sum('cash'))

