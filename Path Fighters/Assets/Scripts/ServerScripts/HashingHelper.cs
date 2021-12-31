using System.Security.Cryptography;
using System.Text;
using System;

public class HashingHelper : IDisposable
    {
        private HashAlgorithm _hashAlgorithm;

        public HashingHelper(HashAlgorithm hashAlgorithm)
        {
            _hashAlgorithm = hashAlgorithm;
        }

        public void Dispose()
        {
            _hashAlgorithm.Dispose();
        }

        public string GenerateHash(string value)
        {
            var strBuilder = new StringBuilder();
            foreach (byte b in _hashAlgorithm.ComputeHash(Encoding.UTF8.GetBytes(value)))
                strBuilder.Append(b.ToString("X2"));
            return strBuilder.ToString();
        }

        public static string GenerateSHA256(string value)
        {
            using (var sha256 = new SHA256Managed())
            {
                return new HashingHelper(sha256).GenerateHash(value);
            }
        }
    }