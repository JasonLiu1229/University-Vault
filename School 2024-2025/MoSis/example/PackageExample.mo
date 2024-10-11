package PackageExample
    model ExampleCode "Cooling example with physical types"
    // Types
    type ConvectionCoefficient = Real(unit = "W/(m2.K)", min = 0);
    type SpecificHeat = Real(unit = "J/(K.kg)", min = 0);
    // Parameters
    parameter Modelica.Units.SI.Temperature T_inf = 298.15 "Ambient temperature";
    parameter Modelica.Units.SI.Temperature T0 = 363.15 "Initial temperature";
    parameter ConvectionCoefficient h = 0.7 "Convective cooling coefficient";
    parameter Modelica.Units.SI.Area A = 1.0 "Surface area";
    parameter Modelica.Units.SI.Mass m = 0.1 "Mass of thermal capacitance";
    parameter SpecificHeat c_p = 1.2 "Specific heat";
    // Variables
    Modelica.Units.SI.Temperature T "Temperature";
  initial equation
    T = T0 "Specify initial value for T";
  equation
    m*c_p*der(T) = h*A*(T_inf - T) "Newton's law of cooling";
  end ExampleCode;

  block coolingBlock
    extends ExampleCode;
    extends Modelica.Blocks.Interfaces.SO;
    
    equation
      y = T;
  end coolingBlock;

  model causal_loop
    coolingBlock coolingBlock1 annotation(
      Placement(transformation(origin = {-28, 34}, extent = {{-10, -10}, {10, 10}})));
    coolingBlock coolingBlock2 annotation(
      Placement(transformation(origin = {-28, -8}, extent = {{-10, -10}, {10, 10}})));
    Modelica.Blocks.Math.Add add annotation(
      Placement(transformation(origin = {40, 12}, extent = {{-10, -10}, {10, 10}})));
  equation
  connect(coolingBlock1.y, add.u1) annotation(
      Line(points = {{-16, 34}, {28, 34}, {28, 18}}, color = {0, 0, 127}));
  connect(coolingBlock2.y, add.u2) annotation(
      Line(points = {{-16, -8}, {28, -8}, {28, 6}}, color = {0, 0, 127}));
  end causal_loop;
  annotation(
    uses(Modelica(version = "4.0.0")));
end PackageExample;