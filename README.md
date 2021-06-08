# Objects_public AWS Lambda based on S3 events

### Criar uma role com as devidas permissões
![image](https://user-images.githubusercontent.com/30154971/121263948-c6219b80-c88c-11eb-8c54-db5734cb662b.png)

![image](https://user-images.githubusercontent.com/30154971/121263985-d46fb780-c88c-11eb-9a2a-8d1997472481.png)

![image](https://user-images.githubusercontent.com/30154971/121264017-de91b600-c88c-11eb-9c30-cda90f6fc51c.png)

![image](https://user-images.githubusercontent.com/30154971/121264056-ef422c00-c88c-11eb-8b25-1224723b9c07.png)

![image](https://user-images.githubusercontent.com/30154971/121264102-02ed9280-c88d-11eb-9da3-6e617585f5f5.png)

![image](https://user-images.githubusercontent.com/30154971/121264128-0ed95480-c88d-11eb-88a8-09e7906cb836.png)

### Copie e cole o codigo e ajuste o bucket-name, conforme imagem abaixo 

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": [
                "arn:aws:s3:::bucket-name/*"
            ]
        }
    ]
}
```


![image](https://user-images.githubusercontent.com/30154971/121264214-34665e00-c88d-11eb-85bd-10bddb5e044f.png)



### Criar a funtion lambda, passando o nome + runtime + role qual foi criada 


![image](https://user-images.githubusercontent.com/30154971/121264599-c40c0c80-c88d-11eb-88dc-2555981888c7.png)

### Configure o código

![image](https://user-images.githubusercontent.com/30154971/121265240-e2263c80-c88e-11eb-920d-c8afbaf8549e.png)

### Configure o time

![image](https://user-images.githubusercontent.com/30154971/121265385-1a2d7f80-c88f-11eb-8e3a-65da81ee4f01.png)


### Com a funtion já criada, configura a trigger

![image](https://user-images.githubusercontent.com/30154971/121263304-cc634800-c88b-11eb-9504-04ed8604b8b3.png)

![image](https://user-images.githubusercontent.com/30154971/121264805-2238ef80-c88e-11eb-825e-f4fb8a60a963.png)

![image](https://user-images.githubusercontent.com/30154971/121264875-4268ae80-c88e-11eb-8670-4f9446e2d0d7.png)




