import xml.etree.ElementTree as ET

class RecordExcel:
    id = 0
    gt = 0
    ai = 0
    advice = ""
    contesto = ""
    assessmentA = []
    assessmentR = []
    etichetta = ""
    esempio = ""

    def parseAssessment(self, assessmentValue):
        print(assessmentValue)
        content = """
        <test>
            <temp><!{}></temp>
            <temp><!{}></temp>
        </test>
        """.format(assessmentValue[0] ,assessmentValue[1])
        tree = ET.fromstring(content)
        listaAssessment = []
        for node in tree.iter('temp'):
            listaAssessment.append(node.text)
        return listaAssessment

    def paragrafoContesto(self, contesto):
        if( contesto == "Accuratezza"):
            return "<p>Si consideri che la macchina ha una accuratezza di circa il <strong>75%</strong> e sensitività e specificità del 67%. </p>"
        if( contesto == "falsinegativi"):
            return "<p>Si consideri che la macchina sbaglia circa un negativo su 3 (cioè i falsi negativi sono il 33%) </p>"
        if( contesto == "falsipositivi"):
            return "<p>Si consideri che la macchina sbaglia circa un positivo su 3 (cioè i falsi positivi sono il 33%) </p>"

    def __init__(self, id=None, gt=None, ai=None, advice=None, contesto=None, assessmentA=None, assessmentR=None,  etichetta=None, esempio=None):
        self.id = id
        self.gt = gt
        self.ai = ai
        self.advice = advice
        self.contesto = self.paragrafoContesto(contesto)
        tempAssessmentA = assessmentA if assessmentA != None else None
        if tempAssessmentA != None:
            tempAssessmentA = tempAssessmentA.replace("]]", "]]|", 1)
            listaAssessmentA = tempAssessmentA.split("|")
            self.assessmentA = self.parseAssessment(listaAssessmentA)
        tempAssessmentR = assessmentR if assessmentR != None else None
        if tempAssessmentR != None:
            tempAssessmentR = tempAssessmentR.replace("]]", "]]|", 1)
            listaAssessmentR = tempAssessmentR.split("|")
            self.assessmentR = self.parseAssessment(listaAssessmentR)
        else:
            self.assessmentA = None
            self.assessmentR = None
        self.etichetta = etichetta
        self.esempio = esempio

    def __len__(self):
        attributes = [self.id, self.gt, self.ai, self.advice, self.contesto, self.assessmentA, self.assessmentR, self.etichetta, self.esempio]
        return len( [attr for attr in attributes if attr is not None] )

    def __str__(self):
        return """{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t""".format(
            self.id, self.gt, self.ai, self.advice, self.contesto, self.assessmentA, self.assessmentR, self.etichetta,
            self.esempio).replace("None", "")