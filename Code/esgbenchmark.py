from flask import Flask,jsonify,request
import jsonpickle

app = Flask(__name__)

class Response:
  def __init__(self, question, esgType,esgIndicators,primaryDetails,secondaryDetails,citationDetails,pageNumber):
    self.question = question
    self.esgType = esgType
    self.esgIndicators = esgIndicators
    self.primaryDetails = primaryDetails
    self.secondaryDetails = secondaryDetails
    self.citationDetails = citationDetails
    self.pageNumber = pageNumber


    
@app.route("/esg/benchmark/upload/<entityName>",methods=['POST'])
def fetchEsgIndicators(entityName) -> str:
    #name = request.args['entityName']   
    print(entityName);
    f = request.files['file']
    f.save(f.filename)
    return jsonpickle.encode(getBenchMarkDetails(),unpicklable=False)
    
def getBenchMarkDetails():
    list = [];
    response1 = Response("ESG Risk Rating for MSCI", "ESGScore","MSCISustainalytics","A 21.0","-","-","2");
    response2 = Response("what is net zero target", "Environment","NetZeroTarget",".","-","-","21")
    response3 = Response("what is the interim emission reduction target", "Environment","InterimEmissionsReductionTarget","A 21.0","-","-","2")
    response4 = Response("what is the Renewable Electricity Target", "Environment","RenewableElectricityTarget","A 21.0","-","-","2")
    response5 = Response("what is the Circularity Stratergy & targets", "Environment","CircularityStratergy","A 21.0","-","-","2")
    response6 = Response("what is the Diversity, Equity and Inclusion target", "Social","DE&ITarget","A 21.0","-","-","2")
    response7 = Response("what is the employee health and Safety audit target", "Goverance","HealthAndSafetyTarget","A 21.0","-","-","2")
    response8 = Response("what is supply audit target", "Goverance","SuppluAuditTarget","A 21.0","-","-","2")
    response9 = Response("what is the SBTi rating", "Reporting","SBTi","A 21.0","-","-","2")
    response10 = Response("what is the CDP rating", "Reporting","CDP","A 21.0","-","-","2")
    response11= Response("what is the GRI rating", "Reporting","GRI","A 21.0","-","-","2")
    response12 = Response("what is the SASB rating", "Reporting","SASB","A 21.0","-","-","2")
    response13 = Response("what is the TCFD rating", "Reporting","TCFD","A 21.0","-","-","2")
    response14 = Response("is the entity focussing on ESG assurance", "Reporting","Assurance","A 21.0","-","-","2")
    list.append(response1);
    list.append(response2);
    list.append(response3);
    list.append(response4);
    list.append(response5);
    list.append(response6);
    list.append(response7);
    list.append(response8);
    list.append(response9);
    list.append(response10);
    list.append(response11);
    list.append(response12);
    list.append(response13);
    list.append(response14);
    return list


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8088, debug=True)