--
-- PostgreSQL database dump
--

-- Dumped from database version 17.2 (Debian 17.2-1.pgdg120+1)
-- Dumped by pg_dump version 17.2 (Debian 17.2-1.pgdg120+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: appliance; Type: TABLE; Schema: public; Owner: postgres_user
--

CREATE TABLE public.appliance (
    applianceid integer NOT NULL,
    name character varying(255),
    houseid integer
);


ALTER TABLE public.appliance OWNER TO postgres_user;

--
-- Name: appliance_applianceid_seq; Type: SEQUENCE; Schema: public; Owner: postgres_user
--

CREATE SEQUENCE public.appliance_applianceid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.appliance_applianceid_seq OWNER TO postgres_user;

--
-- Name: appliance_applianceid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres_user
--

ALTER SEQUENCE public.appliance_applianceid_seq OWNED BY public.appliance.applianceid;


--
-- Name: calendar; Type: TABLE; Schema: public; Owner: postgres_user
--

CREATE TABLE public.calendar (
    calendarid integer NOT NULL,
    title character varying(255),
    description text,
    occurance character varying(50),
    userid integer,
    houseid integer
);


ALTER TABLE public.calendar OWNER TO postgres_user;

--
-- Name: calendar_calendarid_seq; Type: SEQUENCE; Schema: public; Owner: postgres_user
--

CREATE SEQUENCE public.calendar_calendarid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.calendar_calendarid_seq OWNER TO postgres_user;

--
-- Name: calendar_calendarid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres_user
--

ALTER SEQUENCE public.calendar_calendarid_seq OWNED BY public.calendar.calendarid;


--
-- Name: calendaraccess; Type: TABLE; Schema: public; Owner: postgres_user
--

CREATE TABLE public.calendaraccess (
    accessid integer NOT NULL,
    accesstype character varying(50),
    calendarid integer,
    userid integer
);


ALTER TABLE public.calendaraccess OWNER TO postgres_user;

--
-- Name: calendaraccess_accessid_seq; Type: SEQUENCE; Schema: public; Owner: postgres_user
--

CREATE SEQUENCE public.calendaraccess_accessid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.calendaraccess_accessid_seq OWNER TO postgres_user;

--
-- Name: calendaraccess_accessid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres_user
--

ALTER SEQUENCE public.calendaraccess_accessid_seq OWNED BY public.calendaraccess.accessid;


--
-- Name: house; Type: TABLE; Schema: public; Owner: postgres_user
--

CREATE TABLE public.house (
    houseid integer NOT NULL,
    addressline1 character varying(255),
    addressline2 character varying(255),
    city character varying(255)
);


ALTER TABLE public.house OWNER TO postgres_user;

--
-- Name: house_houseid_seq; Type: SEQUENCE; Schema: public; Owner: postgres_user
--

CREATE SEQUENCE public.house_houseid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.house_houseid_seq OWNER TO postgres_user;

--
-- Name: house_houseid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres_user
--

ALTER SEQUENCE public.house_houseid_seq OWNED BY public.house.houseid;


--
-- Name: houseuser; Type: TABLE; Schema: public; Owner: postgres_user
--

CREATE TABLE public.houseuser (
    usertype character varying(50),
    houseid integer NOT NULL,
    userid integer NOT NULL,
    startdate date,
    enddate date
);


ALTER TABLE public.houseuser OWNER TO postgres_user;

--
-- Name: letter; Type: TABLE; Schema: public; Owner: postgres_user
--

CREATE TABLE public.letter (
    letterid integer NOT NULL,
    houseid integer,
    userid integer,
    lettertype character varying(50),
    messagetext text,
    date date
);


ALTER TABLE public.letter OWNER TO postgres_user;

--
-- Name: letter_letterid_seq; Type: SEQUENCE; Schema: public; Owner: postgres_user
--

CREATE SEQUENCE public.letter_letterid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.letter_letterid_seq OWNER TO postgres_user;

--
-- Name: letter_letterid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres_user
--

ALTER SEQUENCE public.letter_letterid_seq OWNED BY public.letter.letterid;


--
-- Name: measurement; Type: TABLE; Schema: public; Owner: postgres_user
--

CREATE TABLE public.measurement (
    "timestamp" timestamp without time zone NOT NULL,
    key character varying(255),
    value character varying(255),
    sensorid integer NOT NULL
);


ALTER TABLE public.measurement OWNER TO postgres_user;

--
-- Name: sensor; Type: TABLE; Schema: public; Owner: postgres_user
--

CREATE TABLE public.sensor (
    sensorid integer NOT NULL,
    name character varying(255),
    metadata text,
    houseid integer,
    applianceid integer
);


ALTER TABLE public.sensor OWNER TO postgres_user;

--
-- Name: sensor_sensorid_seq; Type: SEQUENCE; Schema: public; Owner: postgres_user
--

CREATE SEQUENCE public.sensor_sensorid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.sensor_sensorid_seq OWNER TO postgres_user;

--
-- Name: sensor_sensorid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres_user
--

ALTER SEQUENCE public.sensor_sensorid_seq OWNED BY public.sensor.sensorid;


--
-- Name: subscribe; Type: TABLE; Schema: public; Owner: postgres_user
--

CREATE TABLE public.subscribe (
    subscriptionid integer NOT NULL,
    eventmeasurement character varying(255),
    "interval" integer,
    threshold double precision,
    applianceid integer,
    userid integer
);


ALTER TABLE public.subscribe OWNER TO postgres_user;

--
-- Name: subscribe_subscriptionid_seq; Type: SEQUENCE; Schema: public; Owner: postgres_user
--

CREATE SEQUENCE public.subscribe_subscriptionid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.subscribe_subscriptionid_seq OWNER TO postgres_user;

--
-- Name: subscribe_subscriptionid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres_user
--

ALTER SEQUENCE public.subscribe_subscriptionid_seq OWNED BY public.subscribe.subscriptionid;


--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres_user
--

CREATE TABLE public.users (
    userid integer NOT NULL,
    firstname character varying(255),
    lastname character varying(255),
    email character varying(255),
    password character varying(255)
);


ALTER TABLE public.users OWNER TO postgres_user;

--
-- Name: users_userid_seq; Type: SEQUENCE; Schema: public; Owner: postgres_user
--

CREATE SEQUENCE public.users_userid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.users_userid_seq OWNER TO postgres_user;

--
-- Name: users_userid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres_user
--

ALTER SEQUENCE public.users_userid_seq OWNED BY public.users.userid;


--
-- Name: appliance applianceid; Type: DEFAULT; Schema: public; Owner: postgres_user
--

ALTER TABLE ONLY public.appliance ALTER COLUMN applianceid SET DEFAULT nextval('public.appliance_applianceid_seq'::regclass);


--
-- Name: calendar calendarid; Type: DEFAULT; Schema: public; Owner: postgres_user
--

ALTER TABLE ONLY public.calendar ALTER COLUMN calendarid SET DEFAULT nextval('public.calendar_calendarid_seq'::regclass);


--
-- Name: calendaraccess accessid; Type: DEFAULT; Schema: public; Owner: postgres_user
--

ALTER TABLE ONLY public.calendaraccess ALTER COLUMN accessid SET DEFAULT nextval('public.calendaraccess_accessid_seq'::regclass);


--
-- Name: house houseid; Type: DEFAULT; Schema: public; Owner: postgres_user
--

ALTER TABLE ONLY public.house ALTER COLUMN houseid SET DEFAULT nextval('public.house_houseid_seq'::regclass);


--
-- Name: letter letterid; Type: DEFAULT; Schema: public; Owner: postgres_user
--

ALTER TABLE ONLY public.letter ALTER COLUMN letterid SET DEFAULT nextval('public.letter_letterid_seq'::regclass);


--
-- Name: sensor sensorid; Type: DEFAULT; Schema: public; Owner: postgres_user
--

ALTER TABLE ONLY public.sensor ALTER COLUMN sensorid SET DEFAULT nextval('public.sensor_sensorid_seq'::regclass);


--
-- Name: subscribe subscriptionid; Type: DEFAULT; Schema: public; Owner: postgres_user
--

ALTER TABLE ONLY public.subscribe ALTER COLUMN subscriptionid SET DEFAULT nextval('public.subscribe_subscriptionid_seq'::regclass);


--
-- Name: users userid; Type: DEFAULT; Schema: public; Owner: postgres_user
--

ALTER TABLE ONLY public.users ALTER COLUMN userid SET DEFAULT nextval('public.users_userid_seq'::regclass);


--
-- Data for Name: appliance; Type: TABLE DATA; Schema: public; Owner: postgres_user
--

COPY public.appliance (applianceid, name, houseid) FROM stdin;
1	Washing Machine	1
2	Washing Machine	2
3	Refrigerator	1
4	Dishwasher	2
5	Microwave	2
6	Air Conditioner	3
7	Heater	4
8	Water Heater	4
9	Fan	5
10	TV	5
11	Oven	6
\.


--
-- Data for Name: calendar; Type: TABLE DATA; Schema: public; Owner: postgres_user
--

COPY public.calendar (calendarid, title, description, occurance, userid, houseid) FROM stdin;
1	Weekly Maintenance	House cleaning every week.	repeat	1	1
2	Monthly Rent Collection	Collect rent from tenants.	repeat	2	2
3	Annual Inspection	Yearly house inspection.	one-time	3	3
\.


--
-- Data for Name: calendaraccess; Type: TABLE DATA; Schema: public; Owner: postgres_user
--

COPY public.calendaraccess (accessid, accesstype, calendarid, userid) FROM stdin;
\.


--
-- Data for Name: house; Type: TABLE DATA; Schema: public; Owner: postgres_user
--

COPY public.house (houseid, addressline1, addressline2, city) FROM stdin;
1	123 Elm Street	Suite 100	New York
2	456 Maple Avenue	Building B	Los Angeles
3	789 Oak Lane		Chicago
4	111 Pine Street		San Francisco
5	222 Cedar Avenue		Boston
6	111 Pine Street		San Francisco
7	222 Cedar Avenue		Boston
8	Malteserplatz	16	Amberg
\.


--
-- Data for Name: houseuser; Type: TABLE DATA; Schema: public; Owner: postgres_user
--

COPY public.houseuser (usertype, houseid, userid, startdate, enddate) FROM stdin;
owner	1	1	2025-01-01	\N
resident	2	2	2025-01-01	2025-12-31
resident	3	3	2025-02-01	\N
owner	5	1	2025-01-01	\N
resident	6	2	2025-01-01	\N
\.


--
-- Data for Name: letter; Type: TABLE DATA; Schema: public; Owner: postgres_user
--

COPY public.letter (letterid, houseid, userid, lettertype, messagetext, date) FROM stdin;
\.


--
-- Data for Name: measurement; Type: TABLE DATA; Schema: public; Owner: postgres_user
--

COPY public.measurement ("timestamp", key, value, sensorid) FROM stdin;
\.


--
-- Data for Name: sensor; Type: TABLE DATA; Schema: public; Owner: postgres_user
--

COPY public.sensor (sensorid, name, metadata, houseid, applianceid) FROM stdin;
\.


--
-- Data for Name: subscribe; Type: TABLE DATA; Schema: public; Owner: postgres_user
--

COPY public.subscribe (subscriptionid, eventmeasurement, "interval", threshold, applianceid, userid) FROM stdin;
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres_user
--

COPY public.users (userid, firstname, lastname, email, password) FROM stdin;
8	Ab	Katkiya	ab.katkiya@gmail.com	Ab123
1	John	Doe	john.doe@example.com	newpassword123
2	Jane	Smith	jane.smith@example.com	securepass456
3	Alice	Johnson	alice.johnson@example.com	mypassword789
\.


--
-- Name: appliance_applianceid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres_user
--

SELECT pg_catalog.setval('public.appliance_applianceid_seq', 11, true);


--
-- Name: calendar_calendarid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres_user
--

SELECT pg_catalog.setval('public.calendar_calendarid_seq', 3, true);


--
-- Name: calendaraccess_accessid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres_user
--

SELECT pg_catalog.setval('public.calendaraccess_accessid_seq', 1, false);


--
-- Name: house_houseid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres_user
--

SELECT pg_catalog.setval('public.house_houseid_seq', 8, true);


--
-- Name: letter_letterid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres_user
--

SELECT pg_catalog.setval('public.letter_letterid_seq', 1, false);


--
-- Name: sensor_sensorid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres_user
--

SELECT pg_catalog.setval('public.sensor_sensorid_seq', 1, false);


--
-- Name: subscribe_subscriptionid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres_user
--

SELECT pg_catalog.setval('public.subscribe_subscriptionid_seq', 1, false);


--
-- Name: users_userid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres_user
--

SELECT pg_catalog.setval('public.users_userid_seq', 9, true);


--
-- Name: appliance appliance_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres_user
--

ALTER TABLE ONLY public.appliance
    ADD CONSTRAINT appliance_pkey PRIMARY KEY (applianceid);


--
-- Name: calendar calendar_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres_user
--

ALTER TABLE ONLY public.calendar
    ADD CONSTRAINT calendar_pkey PRIMARY KEY (calendarid);


--
-- Name: calendaraccess calendaraccess_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres_user
--

ALTER TABLE ONLY public.calendaraccess
    ADD CONSTRAINT calendaraccess_pkey PRIMARY KEY (accessid);


--
-- Name: house house_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres_user
--

ALTER TABLE ONLY public.house
    ADD CONSTRAINT house_pkey PRIMARY KEY (houseid);


--
-- Name: houseuser houseuser_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres_user
--

ALTER TABLE ONLY public.houseuser
    ADD CONSTRAINT houseuser_pkey PRIMARY KEY (houseid, userid);


--
-- Name: letter letter_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres_user
--

ALTER TABLE ONLY public.letter
    ADD CONSTRAINT letter_pkey PRIMARY KEY (letterid);


--
-- Name: measurement measurement_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres_user
--

ALTER TABLE ONLY public.measurement
    ADD CONSTRAINT measurement_pkey PRIMARY KEY ("timestamp", sensorid);


--
-- Name: sensor sensor_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres_user
--

ALTER TABLE ONLY public.sensor
    ADD CONSTRAINT sensor_pkey PRIMARY KEY (sensorid);


--
-- Name: subscribe subscribe_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres_user
--

ALTER TABLE ONLY public.subscribe
    ADD CONSTRAINT subscribe_pkey PRIMARY KEY (subscriptionid);


--
-- Name: users users_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres_user
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres_user
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (userid);


--
-- Name: appliance appliance_houseid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres_user
--

ALTER TABLE ONLY public.appliance
    ADD CONSTRAINT appliance_houseid_fkey FOREIGN KEY (houseid) REFERENCES public.house(houseid) ON UPDATE CASCADE;


--
-- Name: calendar calendar_houseid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres_user
--

ALTER TABLE ONLY public.calendar
    ADD CONSTRAINT calendar_houseid_fkey FOREIGN KEY (houseid) REFERENCES public.house(houseid);


--
-- Name: calendar calendar_userid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres_user
--

ALTER TABLE ONLY public.calendar
    ADD CONSTRAINT calendar_userid_fkey FOREIGN KEY (userid) REFERENCES public.users(userid);


--
-- Name: calendaraccess calendaraccess_calendarid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres_user
--

ALTER TABLE ONLY public.calendaraccess
    ADD CONSTRAINT calendaraccess_calendarid_fkey FOREIGN KEY (calendarid) REFERENCES public.calendar(calendarid);


--
-- Name: calendaraccess calendaraccess_userid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres_user
--

ALTER TABLE ONLY public.calendaraccess
    ADD CONSTRAINT calendaraccess_userid_fkey FOREIGN KEY (userid) REFERENCES public.users(userid);


--
-- Name: houseuser houseuser_houseid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres_user
--

ALTER TABLE ONLY public.houseuser
    ADD CONSTRAINT houseuser_houseid_fkey FOREIGN KEY (houseid) REFERENCES public.house(houseid) ON UPDATE CASCADE;


--
-- Name: houseuser houseuser_userid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres_user
--

ALTER TABLE ONLY public.houseuser
    ADD CONSTRAINT houseuser_userid_fkey FOREIGN KEY (userid) REFERENCES public.users(userid) ON UPDATE CASCADE;


--
-- Name: letter letter_houseid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres_user
--

ALTER TABLE ONLY public.letter
    ADD CONSTRAINT letter_houseid_fkey FOREIGN KEY (houseid) REFERENCES public.house(houseid);


--
-- Name: letter letter_userid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres_user
--

ALTER TABLE ONLY public.letter
    ADD CONSTRAINT letter_userid_fkey FOREIGN KEY (userid) REFERENCES public.users(userid);


--
-- Name: measurement measurement_sensorid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres_user
--

ALTER TABLE ONLY public.measurement
    ADD CONSTRAINT measurement_sensorid_fkey FOREIGN KEY (sensorid) REFERENCES public.sensor(sensorid);


--
-- Name: sensor sensor_applianceid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres_user
--

ALTER TABLE ONLY public.sensor
    ADD CONSTRAINT sensor_applianceid_fkey FOREIGN KEY (applianceid) REFERENCES public.appliance(applianceid);


--
-- Name: sensor sensor_houseid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres_user
--

ALTER TABLE ONLY public.sensor
    ADD CONSTRAINT sensor_houseid_fkey FOREIGN KEY (houseid) REFERENCES public.house(houseid);


--
-- Name: subscribe subscribe_applianceid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres_user
--

ALTER TABLE ONLY public.subscribe
    ADD CONSTRAINT subscribe_applianceid_fkey FOREIGN KEY (applianceid) REFERENCES public.appliance(applianceid);


--
-- Name: subscribe subscribe_userid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres_user
--

ALTER TABLE ONLY public.subscribe
    ADD CONSTRAINT subscribe_userid_fkey FOREIGN KEY (userid) REFERENCES public.users(userid);


--
-- PostgreSQL database dump complete
--

