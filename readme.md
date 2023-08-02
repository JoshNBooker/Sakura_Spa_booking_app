{\rtf1\ansi\ansicpg1252\cocoartf2709
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\fnil\fcharset0 HelveticaNeue;\f2\fnil\fcharset0 .SFNS-Regular_wdth_opsz120000_GRAD_wght2580000;
\f3\fnil\fcharset0 .AppleSystemUIFontMonospaced-Regular;}
{\colortbl;\red255\green255\blue255;\red24\green26\blue30;\red255\green255\blue255;}
{\*\expandedcolortbl;;\cssrgb\c12157\c13725\c15686;\cssrgb\c100000\c100000\c100000;}
{\*\listtable{\list\listtemplateid1\listhybrid{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{disc\}}{\leveltext\leveltemplateid1\'01\uc0\u8226 ;}{\levelnumbers;}\fi-360\li720\lin720 }{\listname ;}\listid1}}
{\*\listoverridetable{\listoverride\listid1\listoverridecount0\ls1}}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs48 \cf0 Brief - 
\fs24 \
\
\pard\pardeftab720\sa320\partightenfactor0

\f1\fs32 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 A customer (don\'92t worry about multiple users just yet, we can pretend this is already within a user being logged in) wants to be able to book wellness treatments at their favourite spa.\
\pard\pardeftab720\partightenfactor0

\f2\b\fs36 \cf2 \cb1 \
\pard\pardeftab720\sa320\partightenfactor0
\cf2 \cb3 MVP\
\pard\pardeftab720\sa320\partightenfactor0

\f1\b0\fs32 \cf2 A customer should be able to create a\'a0
\f3\fs27\fsmilli13600 Booking
\f1\fs32 \'a0with a name, date, time, and\'a0
\f3\fs27\fsmilli13600 Treatment
\f1\fs32 . A customer should be able to see all their scheduled treatments and click through on one to edit it or cancel it. A Treatment can just have a name.\
\pard\pardeftab720\partightenfactor0

\f2\b\fs36 \cf2 \cb1 \
\pard\pardeftab720\sa320\partightenfactor0
\cf2 \cb3 Extensions:\
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls1\ilvl0
\f1\b0\fs32 \cf2 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Date and time could be handled as date type instead of as strings\cb1 \
\ls1\ilvl0\cb3 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 A treatment could have a length of time\cb1 \
\ls1\ilvl0\cb3 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Could you try preventing double booking?\
\pard\tx720\pardeftab720\partightenfactor0
\cf2 \cb1 \
FLASK_RUN_HOST=127.0.0.1\
FLASK_RUN_PORT=4999\
}