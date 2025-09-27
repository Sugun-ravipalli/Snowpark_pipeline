import sys
from snowflake.snowpark import Session
sys.path.append("/workspaces/Snowpark_pipeline")
import generic_code.code_library as cl

import importlib
import generic_code.code_library as cl
importlib.reload(cl)
# If you are running this code in Github code spaces you don't need to execute below command,
#sys.path.append('/Users/pradeep/Downloads/Udemy_course_videos/course_2_assignments/Snowpark_pipeline/')

from generic_code import code_library
from cryptography.hazmat.primitives import serialization



# Load private key
with open("rsa_key.p8", "rb") as key:
    p_key = serialization.load_pem_private_key(
        key.read(),
        password=None,
    )

private_key_bytes = p_key.private_bytes(
    encoding=serialization.Encoding.DER,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

# Make connection and create Snowpark session.
# Please mention your snowflake account credentials below,
connection_parameters = {
    "account":"KZYJRAW-EE11046",
    "user":"SUGUNSNOWPARK",
    "private_key": private_key_bytes,
    "role": "ACCOUNTADMIN",
    "warehouse": "COMPUTE_WH",
    "database": "DEMO_DB",
    "schema": "PUBLIC"
}


# Create connection with snowflake and return the session
session = cl.snowconnect(connection_parameters)

session.session_id
session.sql("select current_user").collect()[0][0]
session.get_current_warehouse()
session.get_current_role()



# session.sql("truncate table  session_audit").collect()



