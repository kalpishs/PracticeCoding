import pandas as pd

df = pd.read_csv('/Users/kalpish/Desktop/Base_Platform_Prop_mdf.csv',  header=None)


df = df[df[2].notna()]


df[0] = df[0].apply(lambda x: x.replace('"', ''))
df[0] = df[0].apply(lambda x: x.replace('“', ''))

df[0] = df[0].apply(lambda x: x.replace('”', ''))

df[0] = df[0].apply(lambda x: x.replace('[]', ''))

df[2] = df[2].apply(lambda x: x.replace('"', ''))
df[2] = df[2].apply(lambda x: x.replace('“', ''))
df[2] = df[2].apply(lambda x: x.replace('”', ''))


df = df.drop(columns=[1])

condition = df[2].str.contains('\[', regex=True)

# Replace values based on the condition
df.loc[condition, 2] = 'unsupported'
df = df[df[0] != "hdfs"]
df = df[df[0] != "daily"]
df = df[df[0] != "I3_ENV"]
df = df[df[0] != "PROD-HTTPS"]
df = df[df[0] != "IDMS-UAT-HTTPS"]

java_properties = ""
for index, row in df.iterrows():
    java_properties += f"{row[0]}={row[2]}\n"

# Write properties to a Java properties file
with open("output.properties", "w") as file:
    file.write(java_properties)


print(df.to_string())
print(df.shape)