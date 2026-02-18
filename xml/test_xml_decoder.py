import unittest

from plantscreen.xml_data_class import parse_xml
from plantscreen.xml_models.group_timing import GroupTiming
from plantscreen.xml_models.protocol import Protocol
from plantscreen.xml_models.configuration import Configuration
from plantscreen.xml_models.system_config import Configuration as SystemConfig
from plantscreen.xml_models.tray_type import TAnyShapes
from plantscreen.xml_models.dataset import DataSet


class TestParseXml(unittest.TestCase):
    def test_group_timing(self):
        xml = '''<GroupTiming type="Once"><DateTime>2020-10-03 16:13:48</DateTime></GroupTiming>'''
        obj = parse_xml(xml)
        self.assertIsInstance(obj, GroupTiming)

    def test_protocol(self):
        xml = '''<Protocol>
            <SetLight>
                <Light name="LightMain1" value="16" />
                <Light name="LightMain2" value="0" />
            </SetLight>
            <TrayLoad row="3" count="30" />
            <Measure>
                <AdaptTime>00:00:00</AdaptTime>
                <Prescription id="1" name="Recipe New:1">
                    <IR1 height="Default">
                        <Offset>0</Offset>
                        <Protocol name="Single imaging">(begin-measure (take-image))</Protocol>
                        <Delay>00:00:00</Delay>
                    </IR1>
                    <Analyse>
                        <MaskErosionLevel>1</MaskErosionLevel>
                    </Analyse>
                </Prescription>
                <Batch name="PS90" pid="1" date="2021-08-19" />
                <Tray sid="10-1__1" id="3354" pid="1" />
                <Tray sid="10-12__1" id="3355" pid="1" />
            </Measure>
            <SetLight>
                <Light name="LightMain1" value="0" />
                <Light name="LightMain2" value="0" />
            </SetLight>
        </Protocol>'''
        obj = parse_xml(xml)
        self.assertIsInstance(obj, Protocol)

    def test_configuration(self):
        xml = '''<?xml version="1.0" encoding="utf-8"?>
        <Configuration>
            <WindowingMode>1</WindowingMode>
            <ExtractLines>1</ExtractLines>
            <Focus>10508</Focus>
            <Width>640</Width>
            <Height>710</Height>
            <DefaultZ>0</DefaultZ>
            <MaskCenterX>308</MaskCenterX>
            <MaskCenterY>637</MaskCenterY>
            <Barrel>-0.04</Barrel>
            <MaskRotation>0.0</MaskRotation>
            <ZConversion>1367</ZConversion>
            <RatioCoefficient>0.00123869</RatioCoefficient>
            <BackwardFEC>true</BackwardFEC>
            <FixedX>false</FixedX>
            <FixedXPxMmRatio>0</FixedXPxMmRatio>
            <FixedY>true</FixedY>
            <FixedYPxMmRatio>0.564726962</FixedYPxMmRatio>
            <CenterShift>
                <Item>
                    <Z>0</Z>
                    <XShift>0</XShift>
                    <YShift>0</YShift>
                </Item>
            </CenterShift>
            <ScanLines>710</ScanLines>
            <PositionStart>1300</PositionStart>
            <PositionEnd>0</PositionEnd>
            <ScanSpeed>1770</ScanSpeed>
            <MoveSpeed>1700</MoveSpeed>
            <ScanAxis>Z</ScanAxis>
            <HeatingTempDiff>8.0</HeatingTempDiff>
            <HeatingTime>1200</HeatingTime>
        </Configuration>
        '''
        obj = parse_xml(xml)
        self.assertIsInstance(obj, Configuration)

    def test_system_config(self):
        xml = '''<?xml version="1.0" encoding="utf-8" ?>
        <Configuration>
            <TrayStack>
                <RowCount>9</RowCount>
                <RowCapacity>30</RowCapacity>
            </TrayStack>
            <AdaptChamber>true</AdaptChamber>
            <HeightMeasurement>true</HeightMeasurement>
            <Commands>
                <SetLight>true</SetLight>
                <TrayLoad>true</TrayLoad>
                <TraySwap>true</TraySwap>
                <TrayUnload>false</TrayUnload>
                <Measure>true</Measure>
            </Commands>
            <Lights>
                <Light caption="Load">LightLoad</Light>
                <Light caption="White">LightMain1</Light>
                <Light caption="Red">LightMain2</Light>
                <Light caption="IR">LightMain3</Light>
            </Lights>
            <Pids>
                <PID name="RGBM" caption="RGBM">
                    <View>Side</View>
                    <Turntable>true</Turntable>
                    <AxisZ heightVisible="false">true</AxisZ>
                </PID>
            </Pids>
            <Analyse></Analyse>
        </Configuration>
        '''
        obj = parse_xml(xml)
        self.assertIsInstance(obj, SystemConfig)

    def test_tanyshapes(self):
        xml = '''<?xml version="1.0" encoding="utf-8"?>
        <TAnyShapes width="192" height="664" xratio="1" yratio="1" ps="2.97421469669443" psx="1.67961923" psy="1.77076723317489">
            <TLineShapes />
            <TMultiShapes>
                <TRectangleShape name="left" left="0" top="0" right="90" bottom="316" />
                <TRectangleShape name="right" left="91" top="1" right="180" bottom="316" />
            </TMultiShapes>
        </TAnyShapes>
        '''
        obj = parse_xml(xml)
        self.assertIsInstance(obj, TAnyShapes)

    def test_dataset(self):
        xml = '''
        <DataSet>
            <Item name="latitude" type="double" unit="degree">49.33948096</Item>
            <Item name="longitude" type="double" unit="degree">16.47611234</Item>
            <Item name="distanceToWantedPoint" type="double" unit="meters">0.46</Item>
            <Item name="speed" type="double" unit="km/h">0.4</Item>
        </DataSet>
        '''
        obj = parse_xml(xml)
        self.assertIsInstance(obj, DataSet)


if __name__ == '__main__':
    unittest.main()
