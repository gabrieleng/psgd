from jarvis.db.figshare import data
import os, requests, io, tempfile, zipfile
from jarvis.analysis.stm.tersoff_hamann import TersoffHamannSTM
import matplotlib.pyplot as plt


fls = data("raw_files")


def make_stm_from_pchg(
    jid="JVASP-27851", bias="Positive", filename="stm_image.jpg",min_size=100
):
    filename=jid+"_"+bias+"_"+str(min_size)+".jpg"
    for i in fls["STM"]:
        zip_name = jid + "_" + bias + ".zip"
        if i["name"] == zip_name:
            zip_file_url = i["download_url"]
            r = requests.get(zip_file_url)
            z = zipfile.ZipFile(io.BytesIO(r.content))
            pchg = z.read("PARCHG").decode("utf-8")
            fd, path = tempfile.mkstemp()
            with os.fdopen(fd, "w") as tmp:
                tmp.write(pchg)
            TH_STM = TersoffHamannSTM(
                chg_name=path, min_size=min_size, zcut=None
            )
            t_height = TH_STM.constant_height(filename=filename)
    return filename

filename=make_stm_from_pchg()
print(filename)
plt.imshow(plt.imread(filename))
plt.axis('off')