from urllib.request import urlopen
from bs4 import BeautifulSoup
import unittest

class Test(unittest.TestCase):
    
    #bs = None
    def setUpClass():
        url = "https://www.careopinion.org.au/83029"
        Test.bs = BeautifulSoup(urlopen(url),'html.parser')
    
    def test_title(self):
        # get_title = Test.bs.find('title').get_text()
        # self.assertEqual('Care Opinion',get_title)
        titleTxt = ""
        # Get the title 
        titleTag = Test.bs.find("title")
        for i in titleTag:
            titleTxt += i
        titleT = titleTxt.replace(" | Care Opinion", "")
        actual_title = titleT

        expected_title = "Hospital ED above and beyond"
        self.assertEqual(expected_title, actual_title)

    def test_review(self):
        revHTML = Test.bs.find(id="opinion_body")
        review = revHTML.text.replace("\n","")
        review = review.replace("\r","")

        expected_review = "My specialty team advised I present to the ED for a different presentation of symptoms possibly stemming from my aggressive brain cancer and its management that is being led by Charlie's. The department was heaving with ambulances ramped up and many distressed patients and family members in the waiting room either waiting to be seen or waiting to be able to go in to see their loved ones.</p><p>Given the circumstances, including clearly, in my opinion,  exhausted staff members, I felt my care was as quick as it could have been. It was unfortunate that I sat in the waiting room with a cannula and was called from and returned to the waiting room after a CT contrast. Despite this,  invasive care and results were conducted in a room within ED itself- not the waiting room.</p><p>As a person with terminal brain cancer, my care is primarily managed by Charlie’s but when I need urgent care, I present to ED at Fiona  Stanley. I understand there are specialist hospitals for certain care, but you may sit as a patient in a different catchment. I have experience working in hospitals and understand that the issue is that Fiona Stanley and Charlie’s use different methods for documenting patient care leading to significant delays in teams within and across sites obtaining information vital  to quality patient care. Further,  I have noticed many senior clinical staff are not aware of the methods to navigate the various databases they can access to obtain some of this patient care detail. I believe a single method of documenting all care and decisions regardless of where a patient presents to hospital would improve communication on all levels, including improved efficiency.</p><p>In terms of the business of the hospital, I believe it would be beneficial to have an urgent GP  service available. This way, when the ED gest busy, staff can redirect people who require urgent, but not life-threatening care (such as broken bones,  vomiting/diarrhoea), to the Urgent Care GP for timely assessment and triaging.  This would, in my opinion, reduce ramping and bed block.</p><p>What was good,  however, was that Fiona Stanley ED staff liaised with their Neuro staff. The  Fiona Stanley Neuro staff liaised with Charlie’s Neuro staff. </p><p>While I was waiting in the ED, some people waiting were eating strong-smelling fast food. Some patients were vomiting and nauseous.  I believe people should not be allowed to bring strong-smelling food into the waiting room to reduce the risk of making other patients feel more ill. </p><p>My only other concern was that I saw people with runny noses and coughing who were not wearing a  mask. I understand that COVID19 restrictions have been eased in the area, but flu-like symptoms are still problematic for some patients, particularly when there is a nasty flu virus that has recently been going around. </p><p>Overall, I was incredibly impressed by the way all staff and volunteers attempted to manage patients in the waiting room. Some of what I witnessed was rather distressing,  but personally believe the staff are going above and beyond within the resource restrictions I think they must be working."
        actual_review = review.encode()
        self.assertEqual(expected_review, actual_review)

    def test_time(self):
        expected_time = "2021-08-24,16:39:42Z"
        timediv = Test.bs.find("time")
        timeSub = timediv.attrs["datetime"]
        actual_time = str(timeSub).replace("T", ",")
        self.assertEqual(expected_time, actual_time)

    def test_about(self):
        # location = fullHTML.find_all("span", itemtype="http://schema.org/Organization")
        # for loc in location:
        #     i = loc.find("span", itemprop="name")
        #     locationStr += i.text
        #     locationStr += ", "
        # locationCp = locationStr[:-2]
        # locations = open(id+"About", "ab")
        # locations.write(locationCp.encode())
        # locations.close()
        
        locationStr = ""
        location = Test.bs.find("span", itemtype="http://schema.org/Organization")
        for loc in location:
            loc = Test.bs.find("span", itemprope = "name")
            locationStr += loc.text
            locationStr += ", "
        locationCp = locationStr[:-2]
        actual_location = locationCp.text
        expected_location = "Fiona Stanley Hospital Emergency Department"
        self.assertEqual(expected_location, actual_location)

    def test_activity(self):

        currentList =  Test.bs.find("li", id="subscribers_read_count")
        try:
            currentReadNum = currentList.strong
        except AttributeError:
            pass
        readNum = ""
        for i in currentReadNum:
            try:
                readNum += i
            except:
                pass

        actual_activity = readNum
        expected_activity = "57"
        self.assertEqual(expected_activity, actual_activity)

    def test_progress(self):
        whereReviewUpToTag = Test.bs.find("aside", class_="author-subscriber")
        progress_tag = whereReviewUpToTag.find("p", class_="margin-top-1 margin-bottom-0")
        progress_tag.replace("\r", "")
        progress_tag.replace("\n", "")
        progress_tag.replace(" ", "")
        actual_progress = progress_tag.text
        expected_progress = "This story has had 2 responses"
        self.assertEqual(expected_progress, actual_progress)

    def test_username(self):
        userNameAll =  Test.bs.find("div", class_="sticky-title inline-block")
        userDiv = userNameAll.find("div")
        userN = userDiv.text.replace("\r","")
        userN = userN.replace("\n","")
        userN = userN.replace("  ","")
        
        actual_username = userN
        expected_username = "Posted By sigmamp55" #changed by to By to match
        self.assertEqual(expected_username, actual_username)
    
    # def test_feel_tag(self):

    # def test_good_tag(self):

    # def test_improved_tag(self):

    # def test_similar_tag(self):

    def test_response(self):
        resp = Test.bs.find("div", id=id.attrs["data-po-response-id"])
        responseHTML = resp.find_all("blockquote", class_="froala-view")

        expected_response = "Dear sigmamp55,Thank you for providing us with such detailed feedback regarding your experience at Fiona Stanley Hospital (FSH) Emergency Department (ED). I am very sorry to read of your diagnosis of terminal cancer, and truly appreciate your insights as having previously worked at hospitals. I also note with thanks the compliments you provided regarding aspects of your care.I did ask the Nurse Unit Manager of the ED to review your post, and although difficult to provide information directly related to you as Care Opinion is anonymous, some of his more broad responses include:It sounds like the Rapid Access Team (RAT) intervened in your case. This is a model of care to assess and manage patients in the waiting room and initiate timely diagnostic interventions that will expedite disposition decisions when patients can access treatment spaces. It is very difficult to manage and police the consumption of food in the waiting room – but your comments are valid and have also raised further hygiene questions for us. Our ED has a specific Consumer Advisory Council for consumer advice on ED-specific business. We have referred this matter to that group for advice and assistance. ED operates a COVID-19 screening process of all patients and visitors that enter. From this assessment process patients are identified for potential influenza type illness symptoms or high-risk factors, and if these criteria are met, instructed to wear a mask and streamlined to an isolated waiting area.Regarding standardised clinical documentation across sites, this would be difficult to achieve since different sites are often managed as separate entities, governed by separate Health Service Boards. I am sure that should the opportunity arise to have consistent documentation tools, it would most certainly be explored by the Department of Health.A St John Urgent Care Clinic is located near to FSH at Cockburn. I understand that there will soon be a campaign to increase public awareness of this and other alternatives to attending an ED for non-life-threatening urgencies.I do wish you all the very best for your ongoing care and treatment.Take care,Neil Doverty Group Executive Director Fiona Stanley Fremantle Hospitals Group"
        actual_response = responseHTML
        self.assertEqual(expected_response, actual_response)

    def test_response_header(self):
        responseHeader = resp.find("div", class_= "inner-expansion-profile")
        expected_responseHeader = "Neil Doverty Executive Director, Fiona Stanley Fremantle Hospitals Group, South Metropolitan Health Service"
        actual_responseHeader = responseHeader
        self.assertEqual(expected_responseHeader, actual_responseHeader)

    def test_response_time(self):
        expected_responseTime = "Submitted on 02/09/2021 at 18:38"
        actual_responseTime = resp.find("span", class_="response-submission-footer-content")
        self.assertEqual(expected_responseTime, actual_responseTime)

    def test_update(self):
        updateDiv = fullHTML.find_all("div", class_="author_response comment public")
        updateHTML = updateDiv.find("blockquote")
        expected_update = "Thank you Neil for your detailed response, advising the actions being taken in response to the issues I noted in my patient story. I believe an urgent GP after hours, in addition to the one located further away from the hospital, is in my opinion, likely not able to be undertaken by the hospital itself, though may be something the wider GP network may consider. Again, given what I witnessed, all ED staff need to be commended on their obvious efforts. I cannot recommend the care I have experienced as a patient at Fiona Stanley highly enough."
        actual_update = updateHTML
        self.assertEqual(expected_update, actual_update)  

    def test_update_time(self):
        updateTime = updateDiv.find("a", class_="share-link")
        expected_updateTime = "Submitted on 03/09/2021 at 11:33 and published on Care Opinion at 11:39"
        actual_updateTime = updateTime
        self.assertEqual(expected_updateTime, actual_updateTime)
    

    def test_content(self):
        pagecontent = Test.bs.find('div',{'id':'container'})
        self.assertIsNotNone(pagecontent)



if __name__ == "__main__":
    unittest.main()