from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'crowdinout_lowfine'
    players_per_group = 5
    multiplier = 2
    fine = 2
    conversion = 0.035
    prac_rounds = 2
    prob_detect = 10
    rounds_interval = 6
    num_rounds = 3 * rounds_interval + 3


class Subsession(BaseSubsession):
    pass


#      def roundnm(self):
#          roundnumber=self.round_number-1
#          return roundnumber
#
# subsessionobj=Subsession(BaseSubsession)

class Group(BaseGroup):
    tot_extraction = models.IntegerField(label="The group's total catch is ")
    individual_share = models.IntegerField(label="At the end of the round, each of you gets extra amount fish of")
    audit = models.IntegerField(label="The person who is randomly audit is player number")
    auditplayer_extrac = models.IntegerField(label="The audited individual's catch is")
    audit_id = models.IntegerField(label="The audited player's id is")

    def set_payoff(self):
        import random
        players = self.get_players()
        extractions = [p.extraction for p in players]
        self.tot_extraction = sum(extractions)
        if (200 - self.tot_extraction) * Constants.multiplier < 200:
            self.individual_share = round(
                (200 - self.tot_extraction) * Constants.multiplier / Constants.players_per_group)
        else:
            self.individual_share = round(200 / Constants.players_per_group)

        for p in players:
            # 10% chance of getting a fine
            if random.randint(1, Constants.prob_detect) == 1 and p.extraction > (
                    100 / Constants.players_per_group) and self.round_number in range(
                    Constants.num_rounds - 2 * Constants.rounds_interval,
                    Constants.num_rounds - Constants.rounds_interval):
                p.individual_fine = int(Constants.fine * (p.extraction - (
                            100 / Constants.players_per_group)))  # determining audited individual's fine and export to the page
                p.payoff = p.extraction + self.individual_share - p.individual_fine
                p.audit_or_not = 1
            else:
                p.individual_fine = 0
                p.audit_or_not = 0
                p.payoff = p.extraction + self.individual_share

        for p in players:
            if self.round_number > 2:
                p.acc_payoff = p.participant.payoff - p.in_round(1).payoff - p.in_round(
                    2).payoff  # participant.payoff is the historical payoff
                p.participant.vars['acc_payoff'] = p.acc_payoff
                # p.act_payoff = p.acc_payoff * Constants.conversion
                # p.actpar_payoff = p.act_payoff + self.session.config['participation_fee']

            # if self.round_number in range(Constants.num_rounds - 12, Constants.num_rounds - 6):
            # self.audit = random.randint(1, Constants.players_per_group)
            # playeraudit = self.get_player_by_id(self.audit)
            # self.auditplayer_extrac = playeraudit.extraction
            # self.audit_id = playeraudit.participant.vars['idnumber']


def quiz1_question(label):
    return models.IntegerField(
        choices=[44, 60, 80, 120],
        widget=widgets.RadioSelect,
        label=label
    )


def quiz2_question(label):
    return models.IntegerField(
        choices=[40, 56, 72, 120],
        widget=widgets.RadioSelect,
        label=label
    )


def quiz3_question(label):
    return models.IntegerField(
        choices=[40, 58, 76, 120],
        widget=widgets.RadioSelect,
        label=label
    )


def quiz4_question(label):
    return models.IntegerField(
        choices=[30, 48, 96, 120],
        widget=widgets.RadioSelect,
        label=label
    )


class Player(BasePlayer):
      id_number = models.IntegerField(label="请填入你的ID 号 (在你桌子的右上角)", min=0, max=300)
      acc_payoff = models.CurrencyField(label="The player's accumulative payoff is ")
      act_payoff = models.CurrencyField(label="The player's accumulative payoff in canadian dollar is")
      actpar_payoff = models.CurrencyField(label="The player's final payoff including the participation fee is")
      extraction = models.IntegerField(label="你这轮决定捕捞多少条鱼", min=0, max=40)
      other_extra = models.IntegerField(label="请同时填写你预期其他组员这一轮的平均捕鱼量", min=0, max=40)
      individual_fine = models.IntegerField(label="The audited indiviudal's fine is ")
      audit_or_not = models.BooleanField(label="The individual is audited or not")
      age = models.IntegerField(label="你的年龄？")
      gender = models.StringField(label="你的性别？",
                                  choices=["男","女","其他","不愿透露"]
      )
      major = models.StringField(
          label="你的专业?"
      )
      income = models.FloatField(label="你的家庭平均月收入是？")
      party = models.StringField(label="你是否是党员？",
                                  choices=["是", "否", "不愿透露"]
                                  )
      volunteer = models.FloatField(label="你去年一年参加的志愿服务活动小时数？")
      strategy = models.StringField(label="当管制实施后，你是否改变了捕捞量？如果改变了，为什么?  如果没有改变，为什么没有改变？",
                                  )
      strategy_repeal = models.StringField(
          label="当管制废除后，与有管制的时候比你是否改变了捕捞量？如果改变了，为什么?  如果没有改变，为什么没有改变？"
          )

      consent = models.BooleanField()  # Record participant's consent.
     # rand_choice = models.IntegerField(label="The decision that is randomly picked by the experimenter")
     # condi_choice = models.IntegerField(
     #     label="what's the contribution for the decision randomly chosen in the last round")
     # other_choice = models.IntegerField(
     #     label="what's others' average contribution in the last round")
      # Quiz QUESTIONS
      # Question 1
      q1 = models.IntegerField(label="", min=0, max=40)
      q2 = models.IntegerField(label="", min=0, max=40)
      q3 = models.IntegerField(
          label="", min=0, max=40)
      q4 = models.IntegerField(
          label="", min=0, max=40)
      q5 = models.IntegerField(
          label="", min=0, max=40)
      q6 = models.IntegerField(
          label="", min=0, max=40)
      q7 = models.IntegerField(
          label="", min=0, max=40)
      q8 = models.IntegerField(
          label="", min=0, max=40)
      q9 = models.IntegerField(
          label="", min=0, max=40)

      quiz1_all = quiz1_question("1. 假设你此轮捕捞了20条鱼，其他组员一共捕捞了120条。此轮中你一共会获得多少条鱼")
      quiz2_all = quiz2_question("2. 假设你此轮捕捞了40条鱼，其他组员一共捕捞了80条。此轮中你一共会获得多少条鱼")

      quiz3_all = quiz3_question(
          "1.  假设你此轮捕捞了30条鱼，其他组员一共捕捞了100条。此轮中你一共会获得多少条鱼")
      quiz4_all = quiz4_question(
          "2.  假设你此轮捕捞了10条鱼，其他组员一共捕捞了140条。此轮中你一共会获得多少条鱼")

      def quiz1_all_error_message(self, quiz1_all):
          if quiz1_all != 44:
              self.participant.vars['quiz'] = 0
              return '你的答案不对。正确答案是44。这是因为小组一共捕捞了140条鱼，湖里剩下60条。此轮最后湖里的鱼数量翻一翻为120条。' \
                     '因此每个组员另外得到24条。你一共得到44条鱼。如果你仍然不明白。请举手向实验人员询问如何解答。我们现在再试两道测试题。现在请选择44，然后继续。'

      def quiz2_all_error_message(self, quiz2_all):
          if quiz2_all != 72:
              self.participant.vars['quiz'] = 0
              return '你的答案不对。正确答案是72。这是因为小组一共捕捞了120条鱼，湖里剩下80条。此轮最后湖里的鱼数量翻一翻为160条。' \
                     '因此每个组员另外得到32条。你一共得到72条鱼。如果你仍然不明白。请举手向实验人员询问如何解答。我们现在再试两道测试题。现在请选择72，然后继续。'

      def quiz3_all_error_message(self, quiz3_all):
          if quiz3_all != 58:
              return '你的答案不对。正确答案是58。这是因为小组一共捕捞了130条鱼，湖里剩下70条。此轮最后湖里的鱼数量翻一翻为140条。' \
                     '因此每个组员另外得到28条。你一共得到58条鱼。如果你仍然不明白。请举手向实验人员询问如何解答。现在请选择76，然后继续。'

      def quiz4_all_error_message(self, quiz4_all):
          if quiz4_all != 30:
              return '你的答案不对。正确答案是30。这是因为小组一共捕捞了150条鱼，湖里剩下50条。此轮最后湖里的鱼数量翻一翻为100条。' \
                     '因此每个组员另外得到20条。你一共得到30条鱼。如果你仍然不明白。请举手向实验人员询问如何解答。现在请选择96，然后继续。'

