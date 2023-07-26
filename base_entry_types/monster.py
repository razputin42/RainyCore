from ..listable_element import BaseListableEntry, not_srd

MonsterHTMLFormatDict = dict(
    first="""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
    .gradient {
        margin:10px 0px;
    }
    .name {
        font-size:225%;
        font-family:Georgia, serif;
        font-variant:small-caps;
        font-weight:bold;
        color:#A73335;
    }
    .description {
        font-style:italic;    
    }
    .bold {
        font-weight:bold;
    }
    .red {
        color:#A73335;
    }
    table {
        width:100%;
        border:0px;
        border-collapse:collapse;
        color:#A73335;
    }
    th, td {
        width:50px;
        text-align:center;
    }
    .actions {
        font-size:175%;
        font-variant:small-caps;
        margin:17px 0px 0px 0px;
    }
    .hr {
        background: #A73335;
        height:2px;
    }
    .attack_odd {
        margin:10px 0px;
        color: black;
    }
    .attack_even {
        margin:10px 0px;
        color: white;
    }
    .bolditalic {
        font-weight:bold;
        font-style:italic;
    }
    </style>
    </head>
    <body>
    <div contenteditable="true"  style="width:310px; font-family:Arial,Helvetica,sans-serif;font-size:17px;">
    <div class="name"> $name </div>
    <div class="description">$size $type, $alignment</div>

    <div class="gradient"><img scr="assets/linear_gradient.png;" /></div>

    <div class="red">
        <div ><span class="bold red">Armor Class</span><span> $armor_class </span></div>
        <div><span class="bold red">Hit Points</span><span> $hit_points</span></div>
        <div><span class="bold red">Speed</span><span> $speed</span></div>
    </div>

    <div class="gradient"><img scr="assets/linear_gradient.png;" /></div>

    <table cellspacing = "0">
        <tr><th>STR</th> <th>DEX</th><th>CON</th><th>INT</th><th>WIS</th><th>CHA</th></tr>
        <tr><td style="padding: 0 10px;">$str ($str_mod)</td> <td style="padding: 0 10px;">$dex ($dex_mod)</td>
        <td style="padding: 0 10px;">$con ($con_mod)</td><td style="padding: 0 10px;">$int ($int_mod)</td>
        <td style="padding: 0 10px;">$wis ($wis_mod)</td><td style="padding: 0 10px;">$cha ($cha_mod)</td></tr>
    </table>

    <br>
    """,
    desc="""
    <div><span class="bold">$name</span><span> $desc</span></div>  
    """,
    cr="""
    <div><span class="bold">Challenge Rating</span><span> $cr</span><span class="description"> ($xp XP)</span></div>  
    """,
    gradient="""
    <div class="gradient"><img scr="assets/linear_gradient.png;" /></div>
    """,
    special_abilities="""
    <div><span class="bolditalic">$name</span><span> $desc</span></div>
    """,
    second="""    
    <div class="actions red">Actions</div>
    <div class="gradient"><img scr="assets/linear_gradient.png;" /></div>
    """,
    action_odd="""
    <div class="hr"></div>
    <div class="attack_even"><span class="bolditalic">$name</span><span> $text</span></div>    
    """,
    action_even="""
    <div class="attack_odd"><span class="bolditalic">$name</span><span> $text</span></div>    
    """,
    legendary_header="""    
    <div class="actions red">Legendary Actions</div>
    <div class="gradient"><img scr="assets/linear_gradient.png;" /></div>
    """,
    rest="""
    </div>
    </body>
    </html>
    """,
    not_srd=not_srd)


class BaseMonster:
    class Behavior(BaseListableEntry):

        @property
        def attack_bonus(self):
            raise NotImplementedError

        @property
        def description(self):
            raise NotImplementedError

        @property
        def damage_dice(self):
            raise NotImplementedError

        def roll(self):
            raise NotImplementedError

        @property
        def type(self):
            raise NotImplementedError

    def get_challenge_rating(self):
        raise NotImplementedError

    def get_size(self):
        raise NotImplementedError

    def get_type(self):
        raise NotImplementedError

    def get_alignment(self):
        raise NotImplementedError

    def get_armor_class(self):
        raise NotImplementedError

    def get_hit_points(self):
        raise NotImplementedError

    def get_speed(self):
        raise NotImplementedError

    def get_strength(self):
        raise NotImplementedError

    def get_strength_modifier(self):
        raise NotImplementedError

    def get_dexterity(self):
        raise NotImplementedError

    def get_dexterity_modifier(self):
        raise NotImplementedError

    def get_constitution(self):
        raise NotImplementedError

    def get_constitution_modifier(self):
        raise NotImplementedError

    def get_intelligence(self):
        raise NotImplementedError

    def get_intelligence_modifier(self):
        raise NotImplementedError

    def get_wisdom(self):
        raise NotImplementedError

    def get_wisdom_modifier(self):
        raise NotImplementedError

    def get_charisma(self):
        raise NotImplementedError

    def get_charisma_modifier(self):
        raise NotImplementedError

    def get_saving_throws(self):
        raise NotImplementedError

    def get_resistances(self):
        raise NotImplementedError

    def get_immunities(self):
        raise NotImplementedError

    def get_condition_immunities(self):
        raise NotImplementedError

    def get_skills(self):
        raise NotImplementedError

    def get_senses(self):
        raise NotImplementedError

    def get_languages(self):
        raise NotImplementedError

    def get_experience(self):
        raise NotImplementedError

    def get_behaviors(self):
        raise NotImplementedError

    def get_actions(self):
        raise NotImplementedError

    def get_traits(self):
        raise NotImplementedError

    def get_legendary_actions(self):
        raise NotImplementedError

    def perform_attack(self, attack):
        raise NotImplementedError
