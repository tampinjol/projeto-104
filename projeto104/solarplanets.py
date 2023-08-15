import cv2

img=cv2.imread("solar-system.jpg")

cv2.putText(img,
            "sol",
            (100,80),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,255)
            )

cv2.putText(img,
            "mercurio",
            (110,180),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,0,255)
            )

cv2.putText(img,
            "venus",
            (190,270),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,0,255)
            )

cv2.putText(img,
            "terra",
            (300,270),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,0,255)
            )

cv2.putText(img,
            "marte",
            (400,270),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,0,255)
            )

cv2.putText(img,
            "jupiter",
            (500,90),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,0,255)
            )

cv2.putText(img,
            "saturno",
            (720,110),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,0,255)
            )

cv2.putText(img,
            "urano",
            (950,130),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,0,255)
            )

cv2.putText(img,
            "netuno",
            (1080,130),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,0,255)
            )

cv2.imshow("resultado",img)
cv2.waitKey(0)
cv2.imwrite("solar_system_name.jpg",img)