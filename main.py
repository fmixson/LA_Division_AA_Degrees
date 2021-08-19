import pandas as pd

from Degree_Applicable_Electives import DegreeApplicableUnits
from Degree_Completion_Report import DegreeCompletionReport
from GE_Progress_Report import GEProgress
from GE_Requirements import GeRequirements
from Major_Progress import MajorProgress
from Major_Requirements import MajorRequirements
from Student_Info import StudentInfo


# def degree_processing(student_id, courses, major, major1, major1_units, major1_disciplines, major2,
#                       major2_units, major3, major3_units, major4, major4_units, major4_disciplines, major5, major5_units,
#                       major_course_requirements, major_name):
def degree_processing(student_id, courses, major_name, major_course_requirements, **kwargs):
    student = StudentInfo(student_id, courses)
    student.eligible_course_list()
    ge_requirements = GeRequirements(student.degree_applicable_dict)
    ge_requirements.ge_courses_completed('Math_Proficiency')
    ge_requirements.ge_courses_completed('Writing_Proficiency')
    ge_requirements.ge_courses_completed('Health_Proficiency')
    ge_requirements.ge_courses_completed('Reading_Proficiency')
    ge_requirements.ge_courses_completed('Nat_Sci')
    ge_requirements.ge_courses_completed('Soc_Sci')
    # ge_requirements.ge_courses_completed('Beh_Sci')
    ge_requirements.ge_courses_completed('FA_Hum')
    ge_requirements.ge_courses_completed('Comp')
    ge_requirements.ge_courses_completed('Analytic')
    ge_requirements.area_e_ge_requirements()
    major = MajorRequirements(revised_course_list=student.degree_applicable_dict,
                              completed_ge_courses=ge_requirements.completed_ge_courses,
                              major_requirements=major_course_requirements)
    if len(kwargs) == 15:
        major.major_courses_completed(area_name=kwargs['major1'], total_units=kwargs['major1_units'],
                                      number_of_disciplines=kwargs['major1_disciplines'])
        major.major_courses_completed(area_name=kwargs['major2'], total_units=kwargs['major2_units'],
                                      number_of_disciplines=kwargs['major2_disciplines'])
        major.major_courses_completed(area_name=kwargs['major3'], total_units=kwargs['major3_units'],
                                      number_of_disciplines=kwargs['major3_disciplines'])
        major.major_courses_completed(area_name=kwargs['major4'], total_units=kwargs['major4_units'],
                                      number_of_disciplines=kwargs['major4_disciplines'])
        major.major_courses_completed(area_name=kwargs['major5'], total_units=kwargs['major5_units'],
                                      number_of_disciplines=kwargs['major5_disciplines'])
    elif len(kwargs) == 12:
        major.major_courses_completed(area_name=kwargs['major1'], total_units=kwargs['major1_units'],
                                      number_of_disciplines=kwargs['major1_disciplines'])
        major.major_courses_completed(area_name=kwargs['major2'], total_units=kwargs['major2_units'],
                                      number_of_disciplines=kwargs['major2_disciplines'])
        major.major_courses_completed(area_name=kwargs['major3'], total_units=kwargs['major3_units'],
                                      number_of_disciplines=kwargs['major3_disciplines'])
        major.major_courses_completed(area_name=kwargs['major4'], total_units=kwargs['major4_units'],
                                      number_of_disciplines=kwargs['major4_disciplines'])

    elif len(kwargs) == 9:
        major.major_courses_completed(area_name=kwargs['major1'], total_units=kwargs['major1_units'],
                                      number_of_disciplines=kwargs['major1_disciplines'])
        major.major_courses_completed(area_name=kwargs['major2'], total_units=kwargs['major2_units'],
                                      number_of_disciplines=kwargs['major2_disciplines'])
        major.major_courses_completed(area_name=kwargs['major3'], total_units=kwargs['major3_units'],
                                      number_of_disciplines=kwargs['major3_disciplines'])

    elif len(kwargs) == 6:
        major.major_courses_completed(area_name=kwargs['major1'], total_units=kwargs['major1_units'],
                                      number_of_disciplines=kwargs['major1_disciplines'])
        major.major_courses_completed(area_name=kwargs['major2'], total_units=kwargs['major2_units'],
                                      number_of_disciplines=kwargs['major2_disciplines'])

    elif len(kwargs) ==3:
        major.major_courses_completed(area_name=kwargs['major1'], total_units=kwargs['major1_units'],
                                      number_of_disciplines=kwargs['major1_disciplines'])

    degree_applicable_units = DegreeApplicableUnits(student.eligible_course_list(),
                                                    major.major_courses_list,
                                                    ge_requirements.area_e_ge_requirements(),
                                                    ge_requirements.completed_ge_units,
                                                    major.major_units_list)
    degree_applicable_units.elective_courses()
    ge_requirements.reading_proficiency()
    degree_applicable_units = DegreeApplicableUnits(student.eligible_course_list(),
                                                    major.major_courses_list,
                                                    ge_requirements.area_e_ge_requirements(),
                                                    ge_requirements.completed_ge_units,
                                                    major.major_units_list)
    degree_applicable_units.elective_courses()
    ge_requirements.reading_proficiency()
    degree_reports = GEProgress(ge_requirements.completed_ge_courses, ge_requirements.completed_ge_units,
                                student.student_id)
    degree_reports.ge_requirements_completed()
    degree_reports.area_e_requirements_completed()
    degree_reports.area_e_requirements_completed()
    major_report = MajorProgress(student_id=student.student_id,
                                 major_course_dict=major.major_course_dict,
                                 major_units=major.major_units_list,
                                 area_units=major.area_units_dict,
                                 no_of_courses_required=major.major_no_courses_requirement_dict)

    major_report.major_requirements_completed()

    degree_completion = DegreeCompletionReport(
        major_requirements_dict=major.major_requirements_dict,
        completed_ge_courses=ge_requirements.completed_ge_courses,
        completed_ge_units=ge_requirements.completed_ge_units,
        major_course_dict=major.major_course_dict,
        area_units_dict=major.area_units_dict,
        elective_courses=degree_applicable_units.elective_course_list,
        elective_units=degree_applicable_units.elective_units_list,
        major_units_list=major.major_units_list,
        student_id=student_id,
        student_major=major_name,
        missing_ge=degree_reports.missing_ge_courses,
        missing_major_courses=major_report.missing_courses_dict2)
    degree_completion.degree_completion()


#End of function

def sorting_majors(major, major_course_requirements, **kwargs):
    student_id_list = []

    for i in range(len(enrollment_history)):
        if enrollment_history.loc[i, "ID"] not in student_id_list:

            if enrollment_history.loc[i, "Major"] == major:
                student_id_list.append(enrollment_history.loc[i, "ID"])
                print(student_id_list)

    for student_id in student_id_list:
        degree_processing(student_id=student_id, courses=enrollment_history, major_name=major,
                          major_course_requirements=major_course_requirements, **kwargs)


pd.set_option('display.max_columns', None)
student_id_and_major = pd.read_csv(
    "C:/Users/fmixson/Desktop/Programming/Enrollment_Histories/AA_Majors_By_ID.csv")
# print(student_id_and_major)

id_and_major_dict = {}

for i in range(len(student_id_and_major)):
    id_and_major_dict[student_id_and_major.loc[i, "Employee ID"]] = student_id_and_major.loc[i, "Major"]
    # print(id_and_major_dict)

enrollment_history = pd.read_csv(
    "C:/Users/fmixson/Desktop/Programming/Enrollment_Histories/EnrollmentHistory_20210817.csv")

# print(enrollment_history)

"""
Create new column then do for loop with if statement. 
if the id in dictionary matches id in dataframe then put the major in the new column.
"""
for key in id_and_major_dict:
    print(id_and_major_dict)
    print(len(id_and_major_dict))
    for i in range(1, len(enrollment_history)):
        # print(i)
        if key == enrollment_history.loc[i, "ID"]:
            # print(key, enrollment_history.loc[i, "ID"])
            enrollment_history.loc[i, "Major"] = id_and_major_dict[key]
            # print(enrollment_history)

sorting_majors(major="Chinese-AA", major_course_requirements='Chin_AA.csv',
               major1="Core1", major1_units=3, major1_disciplines=1,
               major2="Core2", major2_units=18, major2_disciplines=1)
sorting_majors(major="English-AA", major_course_requirements='English_AA.csv',
               major1="Core1", major1_units=4, major1_disciplines=1,
               major2="Core2", major2_units=3, major2_disciplines=1,
               major3="Lit", major3_units=12, major3_disciplines=1)
sorting_majors(major="American Sign Language-AA", major_course_requirements='ASL_AA.csv',
               major1="Core", major1_units=19, major1_disciplines=1,
               major2="ListA", major2_units=3, major2_disciplines=1)
sorting_majors(major="English/Tran-AA", major_course_requirements='English_AA.csv',
               major1="Core1", major1_units=4, major1_disciplines=1,
               major2="Core2", major2_units=3, major2_disciplines=1,
               major3="Lit", major3_units=12, major3_disciplines=1)
sorting_majors(major="French-AA", major_course_requirements='Fren_AA.csv',
               major1="Core", major1_units=26, major1_disciplines=1)





# pd.set_option('display.max_columns', None)
#
# student_course_list = pd.read_csv(
#     "C:/Users/fmixson/Desktop/Programming/Enrollment_Histories/LA_Division_AA_Degrees.csv")
# student_id_list = []
#
# for i in range(len(student_course_list)):
#     if student_course_list.loc[i, "ID"] not in student_id_list:
#         student_id_list.append(student_course_list.loc[i, "ID"])
#
# for student_id in student_id_list:
#
#         degree_processing(student_id=student_id, courses=student_course_list, major='asl_major_requirements',
#                           major_name="ASL_AA", major_course_requirements="ASL_AA.csv",
#                           major1="Core", major1_units=19, major1_disciplines=1,
#                           major2="ListA", major2_units=3, major2_disciplines=1)
#
#         degree_processing(student_id=student_id, courses=student_course_list, major='chin_major_requirements',
#                           major_name="CHIN_AA", major_course_requirements="Chin_AA.csv",
#                           major1="Core1", major1_units=3, major1_disciplines=1,
#                           major2="Core2", major2_units=18, major2_disciplines=1)
#
#         degree_processing(student_id=student_id, courses=student_course_list, major='comm_AA_major_requirements',
#                           major_name="Comm Studies", major_course_requirements="Comm_AA.csv",
#                           major1="Core1", major1_units=3, major1_disciplines=1,
#                           major2="Core2", major2_units=3, major2_disciplines=1,
#                           major3="ListA", major3_units=6, major3_disciplines=1,
#                           major4="ListB", major4_units=6, major4_disciplines=1)
#
#
#         degree_processing(student_id=student_id, courses=student_course_list, major='english_major_requirements',
#                           major_name="English_AA", major_course_requirements="English_AA.csv",
#                           major1="Core1", major1_units=4, major1_disciplines=1,
#                           major2="Core2", major2_units=3, major2_disciplines=1,
#                           major3="Lit", major3_units=12, major3_disciplines=1)


# DegreeCompletionReport.degree_units_df.sort_values(by=[''], inplace=True, ascending=False)
DegreeCompletionReport.LS_AA_Degrees_df.sort_values(by=['Total_Missing'], inplace=True, ascending=True)
DegreeCompletionReport.LS_AA_Degrees_df.to_csv('C:/Users/fmixson/Desktop/Programming/Units_Sort_Arts_LA_Division_AA_Degrees.csv')
DegreeCompletionReport.LS_AA_Degrees_df.sort_values(by=['Student_ID', 'Total_Missing'], inplace=True, ascending=True)
DegreeCompletionReport.LS_AA_Degrees_df.to_csv('C:/Users/fmixson/Desktop/Programming/Student_Sort_LA_Division_AA_Degrees.csv')
# DegreeCompletionReport.degree_courses_df.to_csv('C:/Users/family/Desktop/Programming/Arts_and_Sciences_AA_Courses.csv')
