// SPDX-License-Identifier: MIT
pragma solidity ^0.8.23;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract Stonks is ERC721, Ownable {

    // ===== Variables =====
    string public baseTokenURI;
    uint256 public mintPrice = 0.0 ether;
    uint256 public collectionSize = 1;
    uint256 private _currentTokenId;

    // Mapping from token ID to owner address
    mapping (uint256 => address) private _owners;

    // ===== Constructor =====
    constructor(address initialOwner) ERC721("Stonks", "STKS") Ownable(initialOwner) {
        _currentTokenId = 0; // Initialize the token ID counter
    }

    // ===== Modifier =====
    function _onlySender() private view {
        require(msg.sender == tx.origin, "Caller is not the transaction origin");
    }

    modifier onlySender {
        _onlySender();
        _;
    }

    // ===== Public mint =====
    function mint(address to, uint256 tokenId) public onlyOwner {
        require(tokenId < collectionSize, "Token ID exceeds collection size");
        require(!_exists(tokenId), "Token ID already exists");

        _safeMint(to, tokenId);
        _owners[tokenId] = to;
    }

    // Manually implement the _exists function
    function _exists(uint256 tokenId) internal view returns (bool) {
        return _owners[tokenId] != address(0);
    }

    // ===== Setter (owner only) =====
    function setMintPrice(uint256 _mintPrice) external onlyOwner {
        mintPrice = _mintPrice;
    }

    function setBaseTokenURI(string memory _baseTokenURI) external onlyOwner {
        baseTokenURI = _baseTokenURI;
    }

    // ===== Withdraw to owner =====
    function withdrawAll() external onlyOwner onlySender {
        (bool success, ) = msg.sender.call{value: address(this).balance}("");
        require(success, "Failed to send ether");
    }

    // ===== View =====
    function tokenURI(uint256 tokenId)
        public
        view
        override
        returns (string memory)
    {
        require(_exists(tokenId), "ERC721Metadata: URI query for nonexistent token");
        return string(abi.encodePacked(baseTokenURI, Strings.toString(tokenId), ".json"));
    }
}
