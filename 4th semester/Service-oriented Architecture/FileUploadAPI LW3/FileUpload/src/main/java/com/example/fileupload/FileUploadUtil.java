package com.example.fileupload;

import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;
import java.io.InputStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;

public class FileUploadUtil {

    public static void saveFile(String fileName, MultipartFile multipartFile) throws IOException {
        Path uploadDirectory = Paths.get("home/root/uploaded");

        try (InputStream inputStream = multipartFile.getInputStream()) {
            Path filepath = uploadDirectory.resolve(fileName);
            Files.copy(inputStream, filepath, StandardCopyOption.REPLACE_EXISTING);
        } catch (IOException ioe) {
            throw new IOException("Error saving uploaded file:" + fileName, ioe);
        }
    }

}
