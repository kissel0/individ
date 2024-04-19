import io
import sys
from random import choice, shuffle

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem
from PyQt5.QtWidgets import QMainWindow

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1000</width>
    <height>200</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: rgb(105, 105, 105);</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QHBoxLayout" name="horizontalLayout">
    <item>
     <widget class="QPushButton" name="add_words">
      <property name="styleSheet">
       <string notr="true">background-color: rgb(255, 250, 250);</string>
      </property>
      <property name="text">
       <string>Добавить слова для изучения </string>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QPushButton" name="my_words">
      <property name="styleSheet">
       <string notr="true">background-color: rgb(255, 250, 250);</string>
      </property>
      <property name="text">
       <string>Слова, возможно, которые вы захотите выучить</string>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QPushButton" name="learn_words">
      <property name="styleSheet">
       <string notr="true">background-color: rgb(255, 250, 250);</string>
      </property>
      <property name="text">
       <string>Слова, которые надо выучить</string>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QPushButton" name="do_test">
      <property name="styleSheet">
       <string notr="true">background-color: rgb(255, 250, 250);</string>
      </property>
      <property name="text">
       <string>Написать тест</string>
      </property>
     </widget>
    </item>
   </layout>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>1000</width>
     <height>22</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""
template1 = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>547</width>
    <height>373</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: rgb(105, 105, 105)</string>
  </property>
  <layout class="QFormLayout" name="formLayout_2">
   <item row="0" column="0">
    <layout class="QVBoxLayout" name="verticalLayout">
     <item>
      <widget class="QLabel" name="label_2">
       <property name="text">
        <string>Слово на русском</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QLineEdit" name="rus_word">
       <property name="styleSheet">
        <string notr="true">background-color: rgb(255, 250, 250)</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QLabel" name="label">
       <property name="text">
        <string>Его перевод на английском </string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QLineEdit" name="trans_engl">
       <property name="styleSheet">
        <string notr="true">background-color: rgb(255, 250, 250)</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="add_text_to_dict">
       <property name="styleSheet">
        <string notr="true">background-color: rgb(255, 250, 250)</string>
       </property>
       <property name="text">
        <string>Добавить</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QLabel" name="line_for_repit">
       <property name="text">
        <string/>
       </property>
      </widget>
     </item>
    </layout>
   </item>
   <item row="0" column="1">
    <widget class="QListWidget" name="dictList">
     <property name="sizePolicy">
      <sizepolicy hsizetype="Preferred" vsizetype="Expanding">
       <horstretch>0</horstretch>
       <verstretch>0</verstretch>
      </sizepolicy>
     </property>
     <property name="styleSheet">
      <string notr="true">background-color: rgb(255, 250, 250)</string>
     </property>
    </widget>
   </item>
  </layout>
 </widget>
 <resources/>
 <connections/>
</ui>
"""
template2 = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>302</width>
    <height>269</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: rgb(105, 105, 105);</string>
  </property>
  <layout class="QVBoxLayout" name="verticalLayout">
   <item>
    <widget class="QTableWidget" name="tableWidget">
     <property name="styleSheet">
      <string notr="true">background-color: rgb(255, 250, 250);</string>
     </property>
     <attribute name="horizontalHeaderCascadingSectionResizes">
      <bool>true</bool>
     </attribute>
     <attribute name="horizontalHeaderStretchLastSection">
      <bool>true</bool>
     </attribute>
     <attribute name="verticalHeaderCascadingSectionResizes">
      <bool>true</bool>
     </attribute>
     <attribute name="verticalHeaderMinimumSectionSize">
      <number>30</number>
     </attribute>
     <attribute name="verticalHeaderDefaultSectionSize">
      <number>30</number>
     </attribute>
     <attribute name="verticalHeaderHighlightSections">
      <bool>false</bool>
     </attribute>
     <attribute name="verticalHeaderStretchLastSection">
      <bool>false</bool>
     </attribute>
     <column>
      <property name="text">
       <string>На английском </string>
      </property>
     </column>
     <column>
      <property name="text">
       <string>На русском</string>
      </property>
     </column>
    </widget>
   </item>
  </layout>
 </widget>
 <resources/>
 <connections/>
</ui>
"""
template3 = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>321</width>
    <height>371</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: rgb(105, 105, 105);</string>
  </property>
  <layout class="QVBoxLayout" name="verticalLayout_3">
   <item>
    <layout class="QVBoxLayout" name="verticalLayout">
     <item>
      <widget class="QLabel" name="label">
       <property name="font">
        <font>
         <pointsize>14</pointsize>
        </font>
       </property>
       <property name="styleSheet">
        <string notr="true">background-color: rgb(255, 250, 250);</string>
       </property>
       <property name="text">
        <string/>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QLineEdit" name="lineEdit">
       <property name="styleSheet">
        <string notr="true">background-color: rgb(255, 250, 250);</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="pushButton">
       <property name="styleSheet">
        <string notr="true">background-color: rgb(255, 250, 250);</string>
       </property>
       <property name="text">
        <string>Ответить</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="pushButton_2">
       <property name="styleSheet">
        <string notr="true">background-color: rgb(255, 250, 250);</string>
       </property>
       <property name="text">
        <string>Следующее слово</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="pushButton_3">
       <property name="styleSheet">
        <string notr="true">background-color: rgb(255, 250, 250);</string>
       </property>
       <property name="text">
        <string>Завершить</string>
       </property>
      </widget>
     </item>
    </layout>
   </item>
   <item>
    <widget class="QLabel" name="line_error">
     <property name="enabled">
      <bool>true</bool>
     </property>
     <property name="sizePolicy">
      <sizepolicy hsizetype="Preferred" vsizetype="Fixed">
       <horstretch>0</horstretch>
       <verstretch>0</verstretch>
      </sizepolicy>
     </property>
     <property name="text">
      <string/>
     </property>
    </widget>
   </item>
  </layout>
 </widget>
 <resources/>
 <connections/>
</ui>
"""
template5 = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>400</width>
    <height>300</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: rgb(105, 105, 105);</string>
  </property>
  <layout class="QVBoxLayout" name="verticalLayout">
   <item>
    <widget class="QPushButton" name="char_Button">
     <property name="styleSheet">
      <string notr="true">background-color: rgb(255, 250, 250);</string>
     </property>
     <property name="text">
      <string>Про характеристики(Цвета и свойства)</string>
     </property>
    </widget>
   </item>
   <item>
    <widget class="QPushButton" name="clothes_Button">
     <property name="styleSheet">
      <string notr="true">background-color: rgb(255, 250, 250);</string>
     </property>
     <property name="text">
      <string>Про одежду</string>
     </property>
    </widget>
   </item>
   <item>
    <widget class="QPushButton" name="time_Button">
     <property name="styleSheet">
      <string notr="true">background-color: rgb(255, 250, 250);</string>
     </property>
     <property name="text">
      <string>Про время</string>
     </property>
    </widget>
   </item>
  </layout>
 </widget>
 <resources/>
 <connections/>
</ui>
"""
template4 = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>409</width>
    <height>325</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: rgb(105, 105, 105);</string>
  </property>
  <layout class="QVBoxLayout" name="verticalLayout">
   <item>
    <widget class="QTableWidget" name="char_table">
     <property name="styleSheet">
      <string notr="true">background-color: rgb(255, 250, 250);</string>
     </property>
     <property name="horizontalScrollBarPolicy">
      <enum>Qt::ScrollBarAlwaysOn</enum>
     </property>
     <attribute name="horizontalHeaderVisible">
      <bool>true</bool>
     </attribute>
     <attribute name="horizontalHeaderCascadingSectionResizes">
      <bool>true</bool>
     </attribute>
     <attribute name="horizontalHeaderHighlightSections">
      <bool>false</bool>
     </attribute>
     <attribute name="horizontalHeaderShowSortIndicator" stdset="0">
      <bool>false</bool>
     </attribute>
     <attribute name="horizontalHeaderStretchLastSection">
      <bool>true</bool>
     </attribute>
     <attribute name="verticalHeaderVisible">
      <bool>false</bool>
     </attribute>
     <attribute name="verticalHeaderCascadingSectionResizes">
      <bool>false</bool>
     </attribute>
     <attribute name="verticalHeaderShowSortIndicator" stdset="0">
      <bool>false</bool>
     </attribute>
     <attribute name="verticalHeaderStretchLastSection">
      <bool>false</bool>
     </attribute>
     <column>
      <property name="text">
       <string>На английском</string>
      </property>
     </column>
     <column>
      <property name="text">
       <string>На русском</string>
      </property>
     </column>
    </widget>
   </item>
  </layout>
 </widget>
 <resources/>
 <connections/>
</ui>
"""
template6 = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>407</width>
    <height>461</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: rgb(105, 105, 105);</string>
  </property>
  <layout class="QVBoxLayout" name="verticalLayout">
   <item>
    <widget class="QTableWidget" name="clothes_table">
     <property name="styleSheet">
      <string notr="true">background-color: rgb(255, 250, 250);</string>
     </property>
     <attribute name="horizontalHeaderCascadingSectionResizes">
      <bool>true</bool>
     </attribute>
     <attribute name="horizontalHeaderStretchLastSection">
      <bool>true</bool>
     </attribute>
     <attribute name="verticalHeaderCascadingSectionResizes">
      <bool>true</bool>
     </attribute>
     <attribute name="verticalHeaderMinimumSectionSize">
      <number>30</number>
     </attribute>
     <attribute name="verticalHeaderDefaultSectionSize">
      <number>30</number>
     </attribute>
     <attribute name="verticalHeaderHighlightSections">
      <bool>false</bool>
     </attribute>
     <attribute name="verticalHeaderStretchLastSection">
      <bool>false</bool>
     </attribute>
     <column>
      <property name="text">
       <string>На английском </string>
      </property>
     </column>
     <column>
      <property name="text">
       <string>На русском</string>
      </property>
     </column>
    </widget>
   </item>
  </layout>
 </widget>
 <resources/>
 <connections/>
</ui>
"""

template7 = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>589</width>
    <height>366</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: rgb(105, 105, 105);</string>
  </property>
  <widget class="QLabel" name="label">
   <property name="geometry">
    <rect>
     <x>200</x>
     <y>110</y>
     <width>271</width>
     <height>141</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true"/>
   </property>
   <property name="text">
    <string>тест будет лёгкий</string>
   </property>
  </widget>
  <widget class="QWidget" name="horizontalLayoutWidget">
   <property name="geometry">
    <rect>
     <x>20</x>
     <y>30</y>
     <width>541</width>
     <height>80</height>
    </rect>
   </property>
   <layout class="QHBoxLayout" name="horizontalLayout_3">
    <item>
     <widget class="QPushButton" name="pushButton">
      <property name="styleSheet">
       <string notr="true">background-color: rgb(255, 250, 250);</string>
      </property>
      <property name="text">
       <string>тест по совим словам</string>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QPushButton" name="pushButton_2">
      <property name="styleSheet">
       <string notr="true">background-color: rgb(255, 250, 250);</string>
      </property>
      <property name="text">
       <string>тест по встроеным словам</string>
      </property>
     </widget>
    </item>
   </layout>
  </widget>
  <widget class="QWidget" name="horizontalLayoutWidget_2">
   <property name="geometry">
    <rect>
     <x>20</x>
     <y>150</y>
     <width>541</width>
     <height>191</height>
    </rect>
   </property>
   <layout class="QHBoxLayout" name="horizontalLayout_5">
    <item>
     <widget class="QLabel" name="label_3">
      <property name="text">
       <string/>
      </property>
      <property name="pixmap">
       <pixmap>C:/Users/kisel/OneDrive/Изображения/Снимки экрана/Снимок экрана 2023-11-08 170817.png</pixmap>
      </property>
      <property name="scaledContents">
       <bool>true</bool>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QLabel" name="label_2">
      <property name="text">
       <string/>
      </property>
      <property name="pixmap">
       <pixmap>C:/Users/kisel/OneDrive/Изображения/Снимки экрана/Снимок экрана 2023-11-08 172955.png</pixmap>
      </property>
      <property name="scaledContents">
       <bool>true</bool>
      </property>
     </widget>
    </item>
   </layout>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""
template8 = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>400</width>
    <height>300</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: rgb(105, 105, 105);
</string>
  </property>
  <layout class="QVBoxLayout" name="verticalLayout_2">
   <item>
    <widget class="QLabel" name="label_2">
     <property name="sizePolicy">
      <sizepolicy hsizetype="Preferred" vsizetype="Fixed">
       <horstretch>0</horstretch>
       <verstretch>0</verstretch>
      </sizepolicy>
     </property>
     <property name="text">
      <string>Выберите правильный вариант(только один)</string>
     </property>
    </widget>
   </item>
   <item>
    <layout class="QHBoxLayout" name="horizontalLayout">
     <item>
      <layout class="QVBoxLayout" name="verticalLayout">
       <item>
        <widget class="QRadioButton" name="rb1">
         <property name="styleSheet">
          <string notr="true">background-color: rgb(255, 250, 250);</string>
         </property>
         <property name="text">
          <string>RadioButton</string>
         </property>
         <attribute name="buttonGroup">
          <string notr="true">buttonGroup</string>
         </attribute>
        </widget>
       </item>
       <item>
        <widget class="QRadioButton" name="rb2">
         <property name="styleSheet">
          <string notr="true">background-color: rgb(255, 250, 250);</string>
         </property>
         <property name="text">
          <string>RadioButton</string>
         </property>
         <attribute name="buttonGroup">
          <string notr="true">buttonGroup</string>
         </attribute>
        </widget>
       </item>
       <item>
        <widget class="QRadioButton" name="rb3">
         <property name="styleSheet">
          <string notr="true">background-color: rgb(255, 250, 250);</string>
         </property>
         <property name="text">
          <string>RadioButton</string>
         </property>
         <attribute name="buttonGroup">
          <string notr="true">buttonGroup</string>
         </attribute>
        </widget>
       </item>
       <item>
        <widget class="QRadioButton" name="rb4">
         <property name="styleSheet">
          <string notr="true">background-color: rgb(255, 250, 250);</string>
         </property>
         <property name="text">
          <string>RadioButton</string>
         </property>
         <attribute name="buttonGroup">
          <string notr="true">buttonGroup</string>
         </attribute>
        </widget>
       </item>
      </layout>
     </item>
     <item>
      <widget class="QLabel" name="label">
       <property name="styleSheet">
        <string notr="true">background-color: rgb(255, 250, 250);</string>
       </property>
       <property name="text">
        <string/>
       </property>
      </widget>
     </item>
    </layout>
   </item>
   <item>
    <widget class="QPushButton" name="pushButton">
     <property name="styleSheet">
      <string notr="true">background-color: rgb(255, 250, 250);</string>
     </property>
     <property name="text">
      <string>Ответить</string>
     </property>
    </widget>
   </item>
   <item>
    <widget class="QPushButton" name="pushButton_2">
     <property name="styleSheet">
      <string notr="true">background-color: rgb(255, 250, 250);
</string>
     </property>
     <property name="text">
      <string>Следущее слово</string>
     </property>
    </widget>
   </item>
   <item>
    <widget class="QPushButton" name="pushButton_3">
     <property name="styleSheet">
      <string notr="true">background-color: rgb(255, 250, 250);</string>
     </property>
     <property name="text">
      <string>Завершить тест</string>
     </property>
    </widget>
   </item>
   <item>
    <widget class="QLabel" name="lineEror">
     <property name="sizePolicy">
      <sizepolicy hsizetype="Preferred" vsizetype="Fixed">
       <horstretch>0</horstretch>
       <verstretch>0</verstretch>
      </sizepolicy>
     </property>
     <property name="text">
      <string/>
     </property>
    </widget>
   </item>
  </layout>
 </widget>
 <resources/>
 <connections/>
 <buttongroups>
  <buttongroup name="buttonGroup"/>
 </buttongroups>
</ui>
"""

temp = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>416</width>
    <height>413</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: rgb(255, 250, 250);</string>
  </property>
  <layout class="QVBoxLayout" name="verticalLayout">
   <item>
    <widget class="QLabel" name="label">
     <property name="sizePolicy">
      <sizepolicy hsizetype="Preferred" vsizetype="Fixed">
       <horstretch>0</horstretch>
       <verstretch>0</verstretch>
      </sizepolicy>
     </property>
     <property name="text">
      <string>Вы успешно прошли тест</string>
     </property>
    </widget>
   </item>
   <item>
    <widget class="QLabel" name="label_2">
     <property name="sizePolicy">
      <sizepolicy hsizetype="Preferred" vsizetype="Fixed">
       <horstretch>0</horstretch>
       <verstretch>0</verstretch>
      </sizepolicy>
     </property>
     <property name="text">
      <string>Вы успешно пополнили свой словарный запас</string>
     </property>
    </widget>
   </item>
   <item>
    <widget class="QLabel" name="label_3">
     <property name="text">
      <string/>
     </property>
     <property name="pixmap">
      <pixmap>мем-великий-гэтсби-оригинал.jpg</pixmap>
     </property>
     <property name="scaledContents">
      <bool>true</bool>
     </property>
    </widget>
   </item>
  </layout>
 </widget>
 <resources/>
 <connections/>
</ui>
"""
temp2 = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>400</width>
    <height>300</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: rgb(255, 250, 250);</string>
  </property>
  <layout class="QVBoxLayout" name="verticalLayout_2">
   <item>
    <layout class="QVBoxLayout" name="verticalLayout">
     <item>
      <widget class="QLabel" name="label">
       <property name="sizePolicy">
        <sizepolicy hsizetype="Preferred" vsizetype="Fixed">
         <horstretch>0</horstretch>
         <verstretch>0</verstretch>
        </sizepolicy>
       </property>
       <property name="text">
        <string>Вы совершили ошибку</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QLabel" name="label_2">
       <property name="sizePolicy">
        <sizepolicy hsizetype="Preferred" vsizetype="Fixed">
         <horstretch>0</horstretch>
         <verstretch>0</verstretch>
        </sizepolicy>
       </property>
       <property name="text">
        <string>Вам стоит потренироватся ещё</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QLabel" name="label_3">
       <property name="text">
        <string/>
       </property>
       <property name="pixmap">
        <pixmap>стонквниз.jpg</pixmap>
       </property>
       <property name="scaledContents">
        <bool>true</bool>
       </property>
      </widget>
     </item>
    </layout>
   </item>
  </layout>
 </widget>
 <resources/>
 <connections/>
</ui>
"""

words_and_translation = {}


# для открытия окон, отходящих от главного окна
class FirstForm(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Главная форма')
        self.setGeometry(500, 500, 1500, 400)

        self.add_words.clicked.connect(self.open_second_form)
        self.learn_words.clicked.connect(self.open_third_form)
        self.do_test.clicked.connect(self.open_fourth_form)
        self.my_words.clicked.connect(self.open_five_form)

    def open_second_form(self):
        self.second_form = Adder(self, "Данные для 2 формы")
        self.second_form.show()

    def open_third_form(self):
        self.third_form = Outputter()
        self.third_form.show()

    def open_fourth_form(self):
        self.fourth_form = ChoseTest()
        self.fourth_form.show()

    def open_five_form(self):
        self.five_form = ChooseThim(self, "Данные для 5 формы")
        self.five_form.show()


# класс для добавления своих слов с словарь
class Adder(QWidget):
    def __init__(self, *args):
        super().__init__()
        f = io.StringIO(template1)
        uic.loadUi(f, self)
        self.initUI(args)

    def initUI(self, args):
        self.setWindowTitle('Выбор')
        self.setGeometry(500, 500, 633, 362)

        self.add_text_to_dict.clicked.connect(self.add_text)

    def add_text(self):

        self.line_for_repit.setText('')
        only_engl = self.trans_engl.text()
        only_rus = self.rus_word.text()
        if only_engl not in words_and_translation and only_rus not in words_and_translation:
            if only_engl.replace(' ', '').isalpha() and only_rus.replace(' ', '').isalpha() and (
                    only_engl.replace(' ', '').isalpha() and only_rus.replace(' ', '').isalpha()):
                self.dictList.addItem(f'{self.trans_engl.text()} - {self.rus_word.text()}')
                words_and_translation[self.trans_engl.text()] = self.rus_word.text()
            else:
                self.line_for_repit.setText('В слове есть постороннии символы. Уберите их')
        else:
            self.line_for_repit.setText('Слово уже находится в словаре')
        self.trans_engl.setText('')
        self.rus_word.setText('')


# для вывода своих слов в таблицу
class Outputter(QWidget):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template2)
        uic.loadUi(f, self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Словарь')
        self.setGeometry(500, 500, 450, 800)

        self.tableWidget.setRowCount(len(words_and_translation))
        words_engl = list(words_and_translation.keys())
        words_rus = list(words_and_translation.values())
        for i in range(len(words_and_translation)):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(words_engl[i]))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(words_rus[i]))


# для выбора темы
class ChooseThim(QWidget):
    def __init__(self, *args):
        super().__init__()
        f = io.StringIO(template5)
        uic.loadUi(f, self)
        self.initUI(args)

    def initUI(self, args):
        self.setWindowTitle('Выбор')
        self.setGeometry(500, 500, 600, 800)

        self.char_Button.clicked.connect(self.open_dict_char)
        self.clothes_Button.clicked.connect(self.open_dict_clothes)
        self.time_Button.clicked.connect(self.open_dict_time)

    def open_dict_char(self):
        self.char_form = Characteristic()
        self.char_form.show()

    def open_dict_clothes(self):
        self.clothes_form = Clothes()
        self.clothes_form.show()

    def open_dict_time(self):
        self.time_form = Time()
        self.time_form.show()


# для вывода слов в таблицу на тему характеристики
class Characteristic(QWidget):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template4)
        uic.loadUi(f, self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Слова')
        self.setGeometry(400, 400, 600, 1000)
        pair_words = []
        new_words = []
        with open('dict_char.txt', encoding="utf8") as f:
            lines = f.readlines()
            for elem in lines:
                line = elem.split('\n')
                pair_words.append(line[0])
        self.char_table.setRowCount(len(pair_words))
        pair_words.sort()
        for elem in pair_words:
            word = elem.split('-')
            new_words.append((word[0], word[1]))
        for i in range(len(new_words)):
            self.char_table.setItem(i, 0, QTableWidgetItem(new_words[i][0]))
            self.char_table.setItem(i, 1, QTableWidgetItem(new_words[i][1]))


# для вывода слов в таблицу на тему одежды
class Clothes(QWidget):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template6)
        uic.loadUi(f, self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Слова')
        self.setGeometry(400, 400, 600, 1000)
        two_words = []
        words = []
        with open('dict_clothes.txt', encoding="utf8") as f:
            lines = f.readlines()
            for elem in lines:
                line = elem.split('\n')
                two_words.append(line[0])
        self.clothes_table.setRowCount(len(two_words))
        two_words.sort()
        for elem in two_words:
            word = elem.split('-')
            words.append((word[0], word[1]))
        for i in range(len(words)):
            self.clothes_table.setItem(i, 0, QTableWidgetItem(words[i][0]))
            self.clothes_table.setItem(i, 1, QTableWidgetItem(words[i][1]))


# для вывода слов в таблицу на тему времени
class Time(QWidget):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template6)
        uic.loadUi(f, self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Слова')
        self.setGeometry(400, 400, 600, 1000)
        two_words1 = []
        words1 = []
        with open('dict_time.txt', encoding="utf8") as f:
            lines = f.readlines()
            for elem in lines:
                line = elem.split('\n')
                two_words1.append(line[0])
        self.clothes_table.setRowCount(len(two_words1))
        two_words1.sort()
        for elem in two_words1:
            word = elem.split('-')
            words1.append((word[0], word[1]))
        for i in range(len(words1)):
            self.clothes_table.setItem(i, 0, QTableWidgetItem(words1[i][0]))
            self.clothes_table.setItem(i, 1, QTableWidgetItem(words1[i][1]))


class ChoseTest(QWidget):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template7)
        uic.loadUi(f, self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Выбор тест')
        self.setGeometry(500, 500, 700, 400)

        self.pushButton.clicked.connect(self.open_test1)
        self.pushButton_2.clicked.connect(self.open_test2)

    def open_test1(self):
        self.testform = Test()
        self.testform.show()

    def open_test2(self):
        self.testform1 = Quizlet()
        self.testform1.show()


class Test(QWidget):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.words_engl = list(words_and_translation.keys())
        self.words_rus = list(words_and_translation.values())
        f = io.StringIO(template3)
        uic.loadUi(f, self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Тест')
        self.setGeometry(500, 500, 450, 800)
        try:
            self.label.setText(self.words_engl[0])
            self.pushButton.clicked.connect(self.true_word)
            self.pushButton_2.clicked.connect(self.next_word)
        except IndexError:
            self.label.setText('Для начала теста добавьте слова')

    def true_word(self):
        if self.label.text() == self.words_engl[0] and self.lineEdit.text() == self.words_rus[0]:
            self.line_error.setText('Перевод сделан правильно')
            self.count += 1
        else:
            self.line_error.setText(f'Перевод сделан не правильно.({self.words_rus[0]})')
            self.count -= 1

    def next_word(self):
        self.lineEdit.setText('')
        self.count_word = len(list(words_and_translation.keys()))
        self.line_error.setText('')
        if len(self.words_engl) != 1:
            del self.words_engl[0]
            del self.words_rus[0]
            self.label.setText(self.words_engl[0])
        else:
            if self.count == self.count_word:
                self.line_error.setText('Слов больше нет. Завершите тест')
                self.pushButton_3.clicked.connect(self.thats_all)
            else:
                self.line_error.setText('Слов больше нет. Завершите тест')
                self.pushButton_3.clicked.connect(self.thats_all_bad)

    def thats_all(self):
        self.form = LittleForm(self, "")
        self.form.show()

    def thats_all_bad(self):
        self.form2 = LittleForm2(self, "")
        self.form2.show()


class LittleForm(QWidget):
    def __init__(self, *args):
        super().__init__()
        f = io.StringIO(temp)
        uic.loadUi(f, self)
        self.initUI(args)

    def initUI(self, args):
        self.setWindowTitle('Итог')
        self.setGeometry(500, 500, 450, 800)


class LittleForm2(QWidget):
    def __init__(self, *args):
        super().__init__()
        f = io.StringIO(temp2)
        uic.loadUi(f, self)
        self.initUI(args)

    def initUI(self, args):
        self.setWindowTitle('Итог')
        self.setGeometry(500, 500, 450, 800)


class Quizlet(QWidget):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template8)
        self.count = 0
        self.answers_count = 0
        self.names = []
        self.true_answer_ind = 0
        self.true_answer = ''
        uic.loadUi(f, self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Итог')
        self.setGeometry(500, 500, 600, 500)
        self.names.clear()
        with open('all_words.txt', encoding="utf8") as f:
            line = f.readlines()
            for i in range(3):
                any_line = choice(line).replace('\n', '').split('-')
                self.names.append(any_line[1])
            word = choice(line).replace('\n', '')
            word = word.split('-')
            self.names.append(word[1])
        self.label.setText(word[0])
        shuffle(self.names)
        self.true_answer_ind = self.names.index(word[1])
        self.true_answer = word[1]

        self.rb1.setText(self.names[0])
        self.rb2.setText(self.names[1])
        self.rb3.setText(self.names[2])
        self.rb4.setText(self.names[3])
        self.pushButton.clicked.connect(self.is_word)
        self.pushButton_2.clicked.connect(self.next_word)

    def all_good(self):
        self.form = LittleForm(self, "")
        self.form.show()

    def all_bad(self):
        self.form2 = LittleForm2(self, "")
        self.form2.show()

    def is_word(self):
        if self.rb1.isChecked():
            if self.rb1.text() == self.true_answer:
                self.count += 1
                self.lineEror.setText('Ответ правильный')
            else:
                self.count -= 1
                self.lineEror.setText(f'Ответ не правильный({self.true_answer})')
        elif self.rb2.isChecked():
            if self.rb2.text() == self.true_answer:
                self.count += 1
                self.lineEror.setText('Ответ правильный')
            else:
                self.count -= 1
                self.lineEror.setText(f'Ответ не правильный({self.true_answer})')

        elif self.rb3.isChecked():
            if self.rb3.text() == self.true_answer:
                self.count += 1
                self.lineEror.setText('Ответ правильный')
            else:
                self.count -= 1
                self.lineEror.setText(f'Ответ не правильный({self.true_answer})')

        elif self.rb4.isChecked():
            if self.rb4.text() == self.true_answer:
                self.count += 1
                self.lineEror.setText('Ответ правильный')

            else:
                self.count -= 1
                self.lineEror.setText(f'Ответ не правильный({self.true_answer})')

    def next_word(self):
        if self.answers_count < 9:
            self.answers_count += 1
            self.lineEror.setText('')
            self.names.clear()
            with open('all_words.txt', encoding="utf8") as f:
                line = f.readlines()
                for i in range(3):
                    any_line = choice(line).replace('\n', '').split('-')
                    self.names.append(any_line[1])
                word = choice(line).replace('\n', '')
                word = word.split('-')
                self.names.append(word[1])
            self.label.setText(word[0])
            shuffle(self.names)
            self.true_answer_ind = self.names.index(word[1])
            self.true_answer = word[1]

            self.rb1.setText(self.names[0])
            self.rb2.setText(self.names[1])
            self.rb3.setText(self.names[2])
            self.rb4.setText(self.names[3])
        else:
            self.lineEror.setText('Завершите тест')
            if self.count == 10:
                self.pushButton_3.clicked.connect(self.all_good)
            else:
                self.pushButton_3.clicked.connect(self.all_bad)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = FirstForm()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
