
import jwt



public_key = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAslHDNkPEF4Xmjz8yd16l
UG15Bhr2YLkh8v6D9OCEvCNRsDq2JFqbAcxCfRnXIKjs/7n2Dv6jaU0X8FP6noEf
GHPyhlLJb/mIk/rTSEatZy0Mf/cbBkF90sJX5dilh/yCn5ygICqJ0egyQJhnrF7w
lp4JnJ2sCXySUaPmX0DyJPfhPuDMT17HktGD+F8e5SbDK8yGeoxqfkdhw5GnSzvI
poCMoSX4h8JUWUevZvKikFI377uuBDkjsuI4D6Mj5BKU7Up6cW/fsKHAWt71s1c0
B2U9tf7FIlN4r5xXSRlk0IKZ9NIvEAr3k3JIFrZQeThu9ITM66Rne9Ndh1HoIOEY
6QIDAQAB
-----END PUBLIC KEY-----"""


access_token = 'eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJtdk9WVUt0WFZxaThIRkItOU1aMnFHbnV5UEhhd3JHZUFBdk15R0hNeXRVIn0.eyJleHAiOjE2MDAxNzc5MDgsImlhdCI6MTYwMDE3NzYwOCwiYXV0aF90aW1lIjoxNjAwMTc3NTAwLCJqdGkiOiI5NzAxMGE4MS0wZjM3LTRkY2ItYmQ1Yi0xNmY0NjAyMDE1ZTciLCJpc3MiOiJodHRwOi8vMTI3LjAuMC4xOjgwMDAvYXV0aC9yZWFsbXMvT2RvbmF0YSIsImF1ZCI6ImFjY291bnQiLCJzdWIiOiJkMjcxNzE2NS00ZjI2LTQ3N2ItYTk5Mi1iYzMxYjJiMDg1Y2QiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJ0aWNrZXQtY2xpZW50Iiwibm9uY2UiOiI1ZGQ4Y2QyNy05NTdhLTQwZGYtOGQzNi1mOGIxM2NmMDBkZTkiLCJzZXNzaW9uX3N0YXRlIjoiYmYzZjhjMTMtOTFjMC00NTgyLWI1NzMtN2YzMmYzMjZhZGU0IiwiYWNyIjoiMCIsImFsbG93ZWQtb3JpZ2lucyI6WyJodHRwOi8vbG9jYWxob3N0OjgwODAiXSwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbIm9mZmxpbmVfYWNjZXNzIiwidW1hX2F1dGhvcml6YXRpb24iXX0sInJlc291cmNlX2FjY2VzcyI6eyJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6Im9wZW5pZCBlbWFpbCBwcm9maWxlIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJtaGVubiJ9.YJOv53HCXrw6GWUfxA0nPzBV-6njx8vQdWSONX3ANuO7b-WxHvq0uhZgcBmks7cvCczSftS0SdZilhGvzuC3TwmxiwKYxNyKo1NUtlqs94J9gPX58thM4ro-On9lK1N5GzpCNkzyO0DF1-YwkIir_EdYRub-S5mGyuTLXBefyakYj-JQ3xMlCyiUqAQchMkoe9Mzk6T_ZEY2rgnGOUn3e2vfbaNkGrR0iPlPDhOHxaNoA7qI2sBG-rIMf23vKtdLuWj_3omtquLMF1DBzSPJ5lrEqryWczYiTfBiBzN2joCglwzcaT9gV67K4YecgKYtg2g3wtkZDYmeaEmlkLep7Q'

print(jwt.decode(access_token, public_key, audience='account'))


