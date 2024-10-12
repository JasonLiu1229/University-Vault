from state.devstate import DevState
from bootstrap.scd import bootstrap_scd
from framework.conformance import Conformance, render_conformance_check_result
from concrete_syntax.textual_od import parser, renderer
from concrete_syntax.common import indent
from concrete_syntax.plantuml import renderer as plantuml
from util.prompt import yes_no, pause

state = DevState()

print("Loading meta-meta-model...")
scd_mmm = bootstrap_scd(state)
print("OK")

print("Is our meta-meta-model a valid class diagram?")
conf = Conformance(state, scd_mmm, scd_mmm)
print(render_conformance_check_result(conf.check_nominal()))

# If you are curious, you can serialize the meta-meta-model:
# print("--------------")
# print(indent(
#     renderer.render_od(state,
#         m_id=scd_mmm,
#         mm_id=scd_mmm),
#     4))
# print("--------------")


# Change this:
factory_mm_cs = """
    Factory:Class {
        
    }
    
    Connectable:Class {
        abstract = True;
    }
    
    provides:Association (Connectable -> Connectable) {
        target_upper_cardinality = 2;
    }
    
    receives:Association (Connectable -> Connectable) {
        target_upper_cardinality = 2;
    }
    
    Source:Class
    :Inheritance (Source -> Connectable)
    
    Sink:Class
    :Inheritance (Sink -> Connectable)
    
    Machine:Class {
        
    }
    :Inheritance (Machine -> Connectable)
    
    Worker:Class {
            
    }
    
    Shift:Class {
            
    }
    
    Currency:Class {
        abstract = True;
    }
    
    Dollar:Class 
    :Inheritance (Dollar -> Currency)
    
    hasWorker:Association (Factory -> Worker) {
        target_lower_cardinality = 1;
    }
    
    hasMachine:Association (Factory -> Machine) {
        target_lower_cardinality = 1;
    }
    
    hasSink:Association (Factory -> Sink) {
        target_lower_cardinality = 1;
        target_upper_cardinality = 1;
    }
    
    hasSource:Association (Factory -> Source) {
        target_lower_cardinality = 1;
        target_upper_cardinality = 1;
    }
    
    workShift:Association (Worker -> Shift) {
        target_lower_cardinality = 1;
        target_upper_cardinality = 2;   
    }  
    
    operates:Association (Worker -> Machine) 
    
    threeShifts:GlobalConstraint {
        constraint = ```
            len(get_all_instances("Shift")) == 3
        ```;
    }
    
    oneMorningShift:GlobalConstraint {
        constraint = ```
            morning_shift = False
            for shift_name, shift_id in get_all_instances("Shift"):
                if shift_name == "morning":
                    morning_shift = True
            morning_shift
        ```;
    }
    
    oneNightShift:GlobalConstraint {
        constraint = ```
            night_shift = False
            for shift_name, shift_id in get_all_instances("Shift"):
                if shift_name == "night":
                    night_shift = True
            night_shift
        ```;
    }
    
    oneAfternoonShift:GlobalConstraint {
        constraint = ```
            afternoon_shift = False
            for shift_name, shift_id in get_all_instances("Shift"):
                if shift_name == "afternoon":
                    afternoon_shift = True
            afternoon_shift
        ```;
    }
    
    outputsToAConnectable:GlobalConstraint {
        constraint = ```
            constraintValid = True
            for machine_name, machine_id in get_all_instances("Machine"):
                if len(get_outgoing(machine_id, "provides")) < 1:
                    constraintValid = False
            constraintValid
        ```;
    }
    
    inputsFromAConnectable:GlobalConstraint {
        constraint = ```
            constraintValid = True
            for machine_name, machine_id in get_all_instances("Machine"):
                if len(get_outgoing(machine_id, "receives")) < 1:
                    constraintValid = False
            constraintValid
        ```;
    }

    thereExistAFactory:GlobalConstraint {
        constraint = ```
            factory_exists = False
            for factory_name, factory_id in get_all_instances("Factory"):
                factory_exists = True
            factory_exists
        ```;
    }
    
    disconnectSinkSource:GlobalConstraint {
        constraint = ```
            constraintValid = True
            for source_name, source_id in get_all_instances("Source"):
                outgoing = get_outgoing(source_id, "provides")
                if len(outgoing) > 0:
                    for link_id in outgoing:
                        target_id = get_target(link_id)
                        if get_type_name(target_id) == "Sink":
                            constraintValid = False
                            
            for sink_name, sink_id in get_all_instances("Sink"):
                outgoing = get_outgoing(sink_id, "receives")
                if len(outgoing) > 0:
                    for link_id in outgoing:
                        target_id = get_target(link_id)
                        if get_type_name(target_id) == "Source":
                            constraintValid = False
                            
            constraintValid
        ```;
    }
    
    sourceNoReceipiant:GlobalConstraint {
        constraint = ```
            constraintValid = True
            for source_name, source_id in get_all_instances("Source"):
                outgoing = get_outgoing(source_id, "receives")
                if len(outgoing) > 0:
                    constraintValid = False
            constraintValid
        ```;
    }
    
    sinkNoProvider:GlobalConstraint {
        constraint = ```
            constraintValid = True
            for sink_name, sink_id in get_all_instances("Sink"):
                outgoing = get_outgoing(sink_id, "provides")
                if len(outgoing) > 0:
                    constraintValid = False
            constraintValid
        ```;
    }
    
    sourceToMachine:GlobalConstraint {
        constraint = ```
            firstCheck = True
            for source_name, source_id in get_all_instances("Source"):
                outgoing = get_outgoing(source_id, "provides")
                if len(outgoing) < 1:
                    firstCheck = False
            
            secondCheck = False
            for machine_name, machine_id in get_all_instances("Machine"):
                outgoing = get_outgoing(machine_id, "receives")
                if len(outgoing) > 0:
                    for link in outgoing:
                        target_id = get_target(link)
                        if get_type_name(target_id) == "Source":
                            secondCheck = True
            
            firstCheck and secondCheck
        ```;
    }
    
    machineToSink:GlobalConstraint {
        constraint = ```
            firstCheck = False
            for machine_name, machine_id in get_all_instances("Machine"):
                outgoing = get_outgoing(machine_id, "provides")
                if len(outgoing) > 0:
                    for link in outgoing:
                        target_id = get_target(link)
                        if get_type_name(target_id) == "Sink":
                            firstCheck = True
            
            secondCheck = False
            for sink_name, sink_id in get_all_instances("Sink"):
                outgoing = get_outgoing(sink_id, "receives")
                if len(outgoing) > 0:
                    for link in outgoing:
                        target_id = get_target(link)
                        if get_type_name(target_id) == "Machine":
                            secondCheck = True
            
            firstCheck and secondCheck
        ```;    
    }
    
    autonomousMachineCheck:GlobalConstraint {
        constraint = ```
            constraintValid = True
            for machine_name, machine_id in get_all_instances("Machine"):
                incoming = get_incoming(machine_id, "operates")
                if len(incoming) >= 1:
                    # check if it has a worker for each shift
                    morning = False
                    afternoon = False
                    night = False
                    for link_id in incoming:
                        worker_id = get_source(link_id)
                        for link_id2 in get_outgoing(worker_id, "workShift"):
                            shift_id = get_target(link_id2)
                            shift_name = get_name(shift_id)
                            if shift_name == "morning":
                                morning = True
                            elif shift_name == "afternoon":
                                afternoon = True
                            elif shift_name == "night":
                                night = True
                    if not (morning and afternoon and night):
                        constraintValid = False
            constraintValid
        ```;
    }
    
    Dollar_amount:AttributeLink (Currency -> Integer) {
        name = "amount";
        optional = False;
        
        constraint = ```
            tgt = get_target(this)
            amount = get_value(tgt)
            amount >= 1000
        ```;
    }
    
    hasSalary:Association (Worker -> Currency) {
        target_lower_cardinality = 1;
    }
    
    
    totalSalary:GlobalConstraint {
        constraint = ```
            constraintValid = True
            for factory_name, factory_id in get_all_instances("Factory"):
                total_salary = 0
                worker_links = get_outgoing(factory_id, "hasWorker")
                for link_id in worker_links:
                    worker_id = get_target(link_id)
                    salary_links = get_outgoing(worker_id, "hasSalary")
                    for link_id2 in salary_links:
                        salary_id = get_target(link_id2)
                        total_salary += get_value(get_slot(salary_id, "amount"))
                if total_salary > 5000:
                    constraintValid = False
            constraintValid
        ```;
    }
    
    everyWorkerBelongsToFactory:GlobalConstraint {
        constraint = ```
            constraintValid = True
            for worker_name, worker_id in get_all_instances("Worker"):
                factory_links = get_incoming(worker_id, "hasWorker")
                if len(factory_links) < 1:
                    constraintValid = False
            constraintValid
        ```;
    }
    
    everyMachineBelongsToFactory:GlobalConstraint {
        constraint = ```
            constraintValid = True
            for machine_name, machine_id in get_all_instances("Machine"):
                factory_links = get_incoming(machine_id, "hasMachine")
                if len(factory_links) < 1:
                    constraintValid = False
            constraintValid
        ```;
    }
    
    machineBelongsToOneFactory:GlobalConstraint {
        constraint = ```
            constraintValid = True
            for machine_name, machine_id in get_all_instances("Machine"):
                factory_links = get_incoming(machine_id, "hasMachine")
                if len(factory_links) != 1:
                    constraintValid = False
            constraintValid
        ```;
    }
    
"""

print()
print("Parsing 'factory' meta-model...")
factory_mm = parser.parse_od(
    state,
    m_text=factory_mm_cs, # the string of text to parse
    mm=scd_mmm, # the meta-model of class diagrams (= our meta-meta-model)
)
print("OK")

# As a double-check, you can serialize the parsed model:
# print("--------------")
# print(indent(
#     renderer.render_od(state,
#         m_id=factory_mm,
#         mm_id=scd_mmm),
#     4))
# print("--------------")

print("Is our 'factory' meta-model a valid class diagram?")
conf = Conformance(state, factory_mm, scd_mmm)
print(render_conformance_check_result(conf.check_nominal()))

# Change this:
factory_m_cs = """

    factory:Factory {   
    }
    
    bob:Worker {     
    }
    
    jon:Worker {
    }
            
    sink1:Sink {
    }
    
    source1:Source {
    }
    
    machine1:Machine {
    }
    
    machine2:Machine {
    }
    
    machine3:Machine {
    }
    
    salary:Dollar {
        amount = 1000;
    }
    
    morning:Shift 
    afternoon:Shift
    night:Shift
    
    :hasWorker (factory -> bob)
    :hasWorker (factory -> jon)
    :hasMachine (factory -> machine1)
    :hasMachine (factory -> machine2)
    :hasMachine (factory -> machine3)
    :hasSink (factory -> sink1)
    :hasSource (factory -> source1)
    
    :workShift (bob -> morning)
    :workShift (bob -> afternoon)
    
    :hasSalary (bob -> salary)
    :hasSalary (jon -> salary)
    
    :workShift (jon -> night)
    
    :operates (bob -> machine1)
    :operates (jon -> machine1)
    
    :provides (source1 -> machine1)
    
    :receives (machine1 -> source1)
    :provides (machine1 -> machine2)
    
    :receives (machine2 -> machine1)
    :provides (machine2 -> machine1)
    :receives (machine1 -> machine2)
    
    :provides (machine2 -> machine3)
    :receives (machine3 -> machine2)
    :provides (machine3 -> sink1)
    
    :receives (sink1 -> machine3)
"""

factory_m_cs_nonconforming = """
    factory:Factory {   
    }
    
    bob:Worker {     
    }
    
    jon:Worker {
    }
            
    sink1:Sink {
    }
    
    source1:Source {
    }
    
    machine1:Machine {
    }
    
    machine2:Machine {
    }
    
    machine3:Machine {
    }
    
    salary1:Dollar {
        amount = 500;
    }
    
    salary2:Dollar {
        amount = 1000;
    }

    morning:Shift 
    midnight:Shift
    
    :hasWorker (factory -> bob)
    
    :hasSalary (bob -> salary1)
    :hasSalary (jon -> salary2)
    
    :workShift (bob -> morning)
    :workShift (jon -> morning)
    
    :hasMachine (factory -> machine1)
    :hasMachine (factory -> machine2)
    :hasMachine (factory -> machine3)
    
    :hasSink (factory -> sink1)
    :hasSource (factory -> source1)
    
    :operates (bob -> machine1)
    :operates (jon -> machine1)
    
    :provides (source1 -> machine1)
    
    :receives (machine1 -> source1)
    :provides (machine1 -> machine2)
    
    :receives (machine2 -> machine1)
    :provides (machine2 -> machine1)
    :receives (machine1 -> machine2)
    
    :provides (machine2 -> machine3)
    :receives (machine3 -> machine2)
    :provides (machine3 -> sink1)
    
    :receives (sink1 -> machine3)
"""

print()
print("Parsing conforming 'factory' model...")
factory_m = parser.parse_od(
    state,
    m_text=factory_m_cs,
    mm=factory_mm, # this time, the meta-model is the previous model we parsed
)
print("OK")

# print()
# print("Parsing non-conforming 'factory' model...")
# factory_m = parser.parse_od(
#     state,
#     m_text=factory_m_cs_nonconforming,
#     mm=factory_mm, # this time, the meta-model is the previous model we parsed
# )
# print("NOT OK")

# As a double-check, you can serialize the parsed model:
# print("--------------")
# print(indent(
#     renderer.render_od(state,
#         m_id=factory_m,
#         mm_id=factory_mm),
#     4))
# print("--------------")

print("Is our model a valid factory-diagram?")
conf = Conformance(state, factory_m, factory_mm)
print(render_conformance_check_result(conf.check_nominal()))


print()
print("==================================")
if yes_no("Print PlantUML?"):
    print_mm = yes_no("  ▸ Print meta-model?")
    print_m = yes_no("  ▸ Print model?")
    print_conf = print_mm and print_m and yes_no("  ▸ Print conformance links?")

    uml = ""
    if print_mm:
        uml += plantuml.render_package("Meta-model", plantuml.render_class_diagram(state, factory_mm))
    if print_m:
        uml += plantuml.render_package("Model", plantuml.render_object_diagram(state, factory_m, factory_mm))
    if print_conf:
        uml += plantuml.render_trace_conformance(state, factory_m, factory_mm)
        
    # write to file
    with open('factory.pu', 'w', encoding='utf-8') as f:
        f.write(uml)

    print("==================================")
    print(uml)
    print("==================================")
    print("Go to http://www.plantuml.com/plantuml/uml/")
    print("and paste the above string.")
