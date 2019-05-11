CREATE USER demo WITH PASSWORD 'demo';


GRANT ALL PRIVILEGES ON DATABASE demo TO demo;

CREATE USER demo_select WITH PASSWORD 'demo_select';
GRANT SELECT ON male_demos TO demo_select WITH GRANT OPTION ;
GRANT SELECT ON female_demos TO demo_select WITH GRANT OPTION ;
GRANT SELECT ON idcodes TO demo_select WITH GRANT OPTION ;
GRANT SELECT ON violent_crimes TO demo_select WITH GRANT OPTION ;
GRANT SELECT ON property_crimes TO demo_select WITH GRANT OPTION ;
GRANT SELECT ON non_hispanic_demos TO demo_select WITH GRANT OPTION ;
GRANT SELECT ON hispanic_demos TO demo_select WITH GRANT OPTION ;
